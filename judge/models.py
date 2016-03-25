from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from authentication.models import User
from problems.models import Problem
from judge.tasks import grade_c_cpp


class Submission(models.Model):
    """
    Submission Model
    """

    problem_id = models.ForeignKey(Problem)
    user_id = models.ForeignKey(User)

    PROCESSING = 0
    AC = 1
    WA = 2
    CE = 3
    RTE = 4
    MLE = 5
    TLE = 6
    SE = 7

    VERDICT_CODE = (
        (PROCESSING, 'Running'),
        (AC, 'Accepted'),
        (WA, 'Wrong Answer'),
        (CE, 'Compilation Error'),
        (RTE, 'Runtime Error'),
        (MLE, 'Memory Limit Exceeded'),
        (TLE, 'Time Limit Exceeded'),
        (SE, 'Internal Server Error')
    )

    C = 0
    CPP = 1
    JAVA = 2
    PYTHON = 3

    LANGUAGE_CODE = (
        (C, 'C'),
        (CPP, 'C++'),
        (JAVA, 'Java'),
        (PYTHON, 'Python')
    )
    code = models.TextField()
    language = models.IntegerField(choices=LANGUAGE_CODE, default=CPP)

    verdict = models.IntegerField(choices=VERDICT_CODE, default=PROCESSING)
    time_taken = models.DecimalField(decimal_places=2, max_digits=3, blank=True, null=True)
    memory_taken = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    error_info = models.TextField(null=True, blank=True)

    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now_add=True)


@receiver(post_save, sender=Submission)
def run_judge(sender, instance, created, **kwargs):
    if created:
        grade_c_cpp.delay(instance)