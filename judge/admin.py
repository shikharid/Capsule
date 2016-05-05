from django.contrib import admin

# Register your models here.
from judge.models import Submission


class SubmissionAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'problem_id',
                    'user_id',
                    'verdict',
                    'language',
                    'created_on',
                    'updated_on')

admin.site.register(Submission, SubmissionAdmin)