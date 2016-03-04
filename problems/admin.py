from django.contrib import admin

# Register your models here.
from problems.models import Problem, Assignment


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



admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Problem, ProblemAdmin)