from django.contrib import admin

# Register your models here.
from problems.models import Problem, Assignment, TestCase


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'assignment_id',
                    'name',
                    'points',
                    'created_on',
                    'updated_on')


class AssignmentAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'faculty_id',
                    'name',
                    'batch_prefix',
                    'deadline',
                    'created_on',
                    'updated_on')


class TestCaseAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'problem_id')

admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(TestCase,TestCaseAdmin)