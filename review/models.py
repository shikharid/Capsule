from django.db import models
# Create your models here.
from problems.models import Assignment, Problem
from authentication.models import User


class PlagiarismRequest(models.Model):
    assignment = models.ForeignKey(Assignment)
    status = models.BooleanField(default=False)

    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now_add=True)


class PlagiarismScore(models.Model):
    problem = models.ForeignKey(Problem)
    student_a = models.ForeignKey(User, related_name='studentA')
    student_b = models.ForeignKey(User, related_name='studentB')
    score = models.FloatField(default=0.0)

    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now_add=True)


class AssignmentReview(models.Model):
    assignment = models.ForeignKey(Assignment)
    student = models.ForeignKey(User)
    review = models.TextField()

    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now_add=True)


class ProblemReview(models.Model):
    problem = models.ForeignKey(Problem)
    student = models.ForeignKey(User)
    review = models.TextField()

    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now_add=True)

