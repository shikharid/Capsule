import os
from django.core.validators import MinValueValidator
from django.db import models
from authentication.models import User


def get_input_file_path(testcase, name):
    return os.path.join('test-case', '{0}.in'.format(testcase.id))


def get_output_file_path(testcase, name):
    return os.path.join('test-case', '{0}.out'.format(testcase.id))


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

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __unicode__(self):
        return self.name


class Problem(models.Model):
    """
    Stores Problem Information of different assignments
    """
    assignment_id = models.ForeignKey(Assignment)
    statement = models.TextField()
    name = models.CharField(max_length=50)
    points = models.IntegerField(validators=[MinValueValidator(0)])

    time_limit = models.DecimalField(decimal_places=1, max_digits=3, validators=[MinValueValidator(1.0)])

    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now_add=True)

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __unicode__(self):
        return self.name


class TestCase(models.Model):
    """
    Stores test cases for problems
    """
    problem_id = models.ForeignKey(Problem)
    input = models.FileField(upload_to=get_input_file_path)
    output = models.FileField(upload_to=get_output_file_path)
    is_used = models.BooleanField(default=True)

    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return '{0} TestCase'.format(self.problem_id.name)