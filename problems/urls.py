from django.conf.urls import patterns, url
from problems import views

urlpatterns = patterns(
    '',
    url(r'^get-pending-assignment-list/$', views.PendingAssignmentAPIView.as_view(), name='pending-list'),
    url(r'^get-completed-assignment-list/$', views.CompletedAssignmentAPIView.as_view(), name='completed-list'),
    url(r'^get-problem-list/$', views.ProblemListAPIView.as_view(), name='problem-list'),

    # Faculty End API endpoints

    url(r'^add-assignment/$', views.AddAssignment.as_view(), name='add-assignment'),
    url(r'^list-assignment/$', views.ListAssignment.as_view(), name='list-assignment'),

    url(r'^assignment/(?P<pk>[\d]+)/edit/$', views.EditAssignment.as_view(), name='edit-assignment'),

    url(r'^assignment/(?P<assignment_id>[\d]+)/problems/$', views.ListProblems.as_view(), name='list-problem'),
    url(r'^assignment/(?P<assignment_id>[\d]+)/problems/add/$',
        views.AddProblems.as_view(),
        name='add-problem'),
    url(r'^assignment/(?P<assignment_id>[\d]+)/problems/(?P<problem_id>[\d]+)/edit/$',
        views.EditProblems.as_view(),
        name='edit-problem'),

    url(r'^assignment/(?P<assignment_id>[\d]+)/problems/(?P<problem_id>[\d]+)/add-testcase/$',
        views.AddTestCase.as_view(),
        name='add-testcase'),
    url(r'^assignment/(?P<assignment_id>[\d]+)/problems/(?P<problem_id>[\d]+)/edit-testcase/$',
        views.EditTestCase.as_view(),
        name='edit-testcase-list'),
    url(r'^assignment/(?P<assignment_id>[\d]+)/problems/(?P<problem_id>[\d]+)/remove-testcase/(?P<id>[\d]+)/$',
        views.RemoveTestCase.as_view(),
        name='remove-testcase'),

)
