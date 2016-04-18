from __future__ import absolute_import
import resource
import subprocess
import tempfile
import cStringIO
import time

from celery.utils.log import get_task_logger
from django.db import transaction

from authentication.models import User, UserScore
from webapp.celery import app
from problems.models import TestCase, ProblemScore, Problem, AssignmentScore

logger = get_task_logger(__name__)

@app.task
@transaction.atomic()
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

        instance, created = ProblemScore.objects.get_or_create(problem=submission_obj.problem_id,
                                                               student=submission_obj.user_id)
        instance.score = submission_obj.problem_id.points if submission_obj.problem_id.points > instance.score \
            else instance.score
        instance.save()

        submission_obj.verdict = 1
        submission_obj.error_info = 'None.Solution Accepted'
        submission_obj.time_taken = total_time
        submission_obj.memory_taken = total_memory
        submission_obj.save()
        return True
    else:
        submission_obj.verdict = 2
        submission_obj.error_info = 'Wrong Answer'
        submission_obj.time_taken = total_time
        submission_obj.save()
        return False


@app.task
@transaction.atomic()
def update_score(assignment):

    if not assignment.review_done:
        return False

    user_queryset = User.objects.filter(member_id__startswith=assignment.batch_prefix)
    user_list = user_queryset.values_list('member_id', flat=True)
    problem_queryset = Problem.objects.filter(assignment_id=assignment)
    problem_list = problem_queryset.values_list('id', flat=True)

    # Gets point for every problem
    def get_points(user_id, problem):
        try:
            score_instance = ProblemScore.objects.get(student__member_id=user_id, problem__id=problem)
            return score_instance.score
        except ProblemScore.DoesNotExist:
            return 0

    def get_score(user_id):
        total = 0
        for problem in problem_list:
            total += get_points(user_id, problem)
        return total

    score = {user: get_score(user) for user in user_list}
    # Update Assignment Score
    for user in user_queryset:
        instance = AssignmentScore(student=user, assignment=assignment, score=score[user.member_id])
        instance.save()

    # Update User Score
    for user in user_queryset:
        instance, created = UserScore.objects.get_or_create(user=user)
        instance.score += score[user.member_id]
        instance.save()
    return True
