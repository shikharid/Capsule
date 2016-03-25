from django.conf.urls import patterns, url
from judge import views

urlpatterns = patterns(
    '',
    url(r'^assignment/(?P<assignment_id>[\d]+)/problems/(?P<problem_id>[\d]+)/submit/$',
        views.SubmissionView.as_view(),
        name='submit-code'),

)
