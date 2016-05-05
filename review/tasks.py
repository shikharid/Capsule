from difflib import SequenceMatcher
import time

from django.db import transaction
from django.db.models import Q
from authentication.models import User
from judge.models import Submission
from problems.models import Problem
from review.models import PlagiarismScore
from webapp.celery import app


@app.task
@transaction.atomic()
def plagiarism_check(plagiarism_instance):
    """
    :param plagiarism_instance plagiarism request instance
    """

    time.sleep(7)  # Humanize check time for presentation
    assignment = plagiarism_instance.assignment
    user_queryset = User.objects.filter(member_id__startswith=assignment.batch_prefix)
    user_list = user_queryset.values_list('member_id', flat=True)
    problem_queryset = Problem.objects.filter(assignment_id=assignment)
    problem_list = problem_queryset.values_list('id', flat=True)

    score = {userA: {userB: {problem: 0.0 for problem in problem_list} for userB in user_list}
             for userA in user_list}

    filter_query = Q(problem_id__in=problem_queryset) & Q(user_id__in=user_queryset) & Q(verdict=Submission.AC)
    submission_queryset = Submission.objects.filter(filter_query).order_by('-updated_on')
    submission_latest = []
    submission_found = {user: {problem: False for problem in problem_list} for user in user_list}

    # Reduce submission list to latest submissions
    for submission in submission_queryset:
        if not submission_found[submission.user_id.member_id][submission.problem_id.id]:
            submission_latest.append(submission)
            submission_found[submission.user_id.member_id][submission.problem_id.id] = True

    # Calculate Matching Ratio
    for submissionA in submission_latest:
        for submissionB in submission_latest:
            if submissionA != submissionB and submissionA.problem_id == submissionB.problem_id:
                user_a = submissionA.user_id.member_id
                user_b = submissionB.user_id.member_id
                problem = submissionA.problem_id.id
                score[user_a][user_b][problem] = SequenceMatcher(None, submissionA.code, submissionB.code).ratio()

    # Update Plagiarism Score for every user
    for user in user_list:
        for problem in problem_queryset:
            max_ratio = 0.0
            max_with = ''
            for user_b in user_list:
                if max_ratio < score[user][user_b][problem.id]:
                    max_ratio = score[user][user_b][problem.id]
                    max_with = user_b
            if max_ratio > 0.0:
                user_a = User.objects.get(member_id=user)
                user_b = User.objects.get(member_id=max_with)
                instance = PlagiarismScore(student_a=user_a, student_b=user_b, problem=problem, score=max_ratio)
                instance.save()
    plagiarism_instance.status = True
    plagiarism_instance.save()
    return True
