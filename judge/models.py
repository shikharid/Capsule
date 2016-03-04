from django.db import models

# Create your models here.
from authentication.models import User
from problems.models import Problem


class Submission(models.Model):
    problem_id = models.ForeignKey(Problem)
    user_id = models.ForeignKey(User)
    spoj_id = models.CharField(max_length=50)
    verdict = models.BooleanField(default=False)