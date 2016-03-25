from __future__ import absolute_import
import resource
import subprocess
import tempfile
import cStringIO
from celery.utils.log import get_task_logger
import time
from webapp.celery import app
from problems.models import TestCase

logger = get_task_logger(__name__)


@app.task
def grade_c_cpp(submission_obj):
    """
    :param submission_id: Database ID of submission
    :param time_limit: Time Limit of submission problem
    """
    # TODO Add support for precision matching
    testcases = TestCase.objects.filter(problem_id=submission_obj.problem_id, is_used=True)  # Selects Test cases
    language = submission_obj.language
    time_limit = submission_obj.problem_id.time_limit

    cmd = 'g++'
    suffix = '.cpp'

    if language == 0:
        cmd = 'gcc'
        suffix = '.c'

    # Set memory limit
    try:
        resource.setrlimit(resource.RLIMIT_DATA, (262144, 262144))
        resource.setrlimit(resource.RLIMIT_STACK, (32768, 65536))
    except resource.error:
        submission_obj.verdict = 7
        submission_obj.error_info = 'Internal Server Error'
        submission_obj.save()
        return False

    # Prepares a temporary cpp file for submission
    code = tempfile.NamedTemporaryFile(suffix=suffix)
    code.write(submission_obj.code)
    code.seek(0)

    # Compiles the temporary file and listens for any compilation errors
    process = subprocess.Popen([cmd, code.name], stderr=subprocess.PIPE)
    result, error = process.communicate()

    # If compilation error is found, saves the error in submission and terminates task
    if error:
        submission_obj.verdict = 3
        submission_obj.error_info = error
        submission_obj.save()
        return False

    flag = True
    total_time = 0.0
    total_memory = 0.0

    system_limit = float(time_limit) + 1.00000  # Time limit normalized for system tasks

    for obj in testcases:

        if not flag:
            break

        start = time.time()  # Time at which execution started

        # The subprocess uses linux timeout command while running the process
        # For running the judge on windows server appropriate changes have to be done
        # System time limit is normalized by 1 second

        process = subprocess.Popen(['timeout', str(system_limit), './a.out'], stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)

        logger.info('Judge process with id {0} running'.format(process.pid))

        user_output, error = process.communicate(input=obj.input.read())
        # process.wait()

        total_memory = max(total_memory, resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)

        total_time += (time.time() - start)    # Calculates elapsed time
        logger.info('Time elapsed for case is {0}'.format(str(time.time() - start)))

        if time.time() > (start + system_limit):
            submission_obj.verdict = 6
            submission_obj.error_info = 'Time Limit Exceeded'
            submission_obj.save()
            return False

        if error:
            submission_obj.verdict = 4
            submission_obj.error_info = 'Runtime Error: {0}'.format(error)
            submission_obj.save()
            return False

        user_output_file = cStringIO.StringIO(user_output)
        expected_output_file = cStringIO.StringIO(obj.output.read())

        # If everything goes well, compares the output and system output files
        while flag:
            l1 = user_output_file.readline().strip()
            l2 = expected_output_file.readline().strip()
            if l1 == '' and l2 == '':
                break
            if l1 != l2:
                flag = False

    code.close()
    # logger.error('Total memory is {0}'.format(total_memory))

    if flag:
        submission_obj.verdict = 1
        submission_obj.error_info = 'None.Solution Accepted'
        submission_obj.time_taken = total_time
        submission_obj.save()
        return True
    else:
        submission_obj.verdict = 2
        submission_obj.error_info = 'Wrong Answer'
        submission_obj.time_taken = total_time
        submission_obj.save()
        return False