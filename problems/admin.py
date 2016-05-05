from django.contrib import admin

# Register your models here.
from problems.models import Problem, Assignment, TestCase, ProblemScore, AssignmentScore


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'assignment_id',
                    'name',
                    'points',
                    'created_on',
                    'updated_on')


class AssignmentAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'review_done',
                    'faculty_id',
                    'name',
                    'batch_prefix',
                    'deadline',
                    'created_on',
                    'updated_on')


class TestCaseAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'problem_id')


class AssignmentScoreAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'assignment',
                    'student',
                    'score')


class ProblemScoreAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'problem',
                    'student',
                    'score')


admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(AssignmentScore, AssignmentScoreAdmin)
admin.site.register(ProblemScore, ProblemScoreAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(TestCase, TestCaseAdmin)