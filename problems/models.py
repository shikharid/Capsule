from django.core.validators import MinValueValidator
from django.db import models
from authentication.models import User


class Assignment(models.Model):
    """
    Stores assignment information
    batch_prefix: member_id prefix of allowed students
    """
    faculty_id = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    subject_code = models.CharField(blank=True, null=True, max_length=15)
    batch_prefix = models.CharField(max_length=50)
    deadline = models.DateField(blank=True, null=True)

    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now_add=True)


class Problem(models.Model):
    """
    Stores Problem Information of different assignments
    """
    assignment_id = models.ForeignKey(Assignment)
    statement = models.CharField(max_length=2000)
    name = models.CharField(max_length=50)
    points = models.IntegerField(validators=[MinValueValidator(0)])

    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now_add=True)


class TestCase(models.Model):
    """
    Stores test cases for problems
    """
    problem_id = models.ForeignKey(Problem)
    input = models.CharField(max_length=1000000)
    output = models.CharField(max_length=1000000)