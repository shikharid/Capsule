from django.contrib import admin

# Register your models here.
from review.models import PlagiarismScore, PlagiarismRequest, ProblemReview, AssignmentReview


class PlagiarismRequestAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'assignment',
                    'status',
                    'created_on',
                    'updated_on')


class ProblemReviewAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'problem',
                    'student',
                    'created_on',
                    'updated_on')


class AssignmentReviewAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'assignment',
                    'student',
                    'created_on',
                    'updated_on')


class PlagiarismScoreAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'student_a',
                    'student_b',
                    'problem',
                    'score',
                    'created_on',
                    'updated_on')

admin.site.register(PlagiarismRequest, PlagiarismRequestAdmin)
admin.site.register(PlagiarismScore, PlagiarismScoreAdmin)
admin.site.register(ProblemReview, ProblemReviewAdmin)
admin.site.register(AssignmentReview, AssignmentReviewAdmin)