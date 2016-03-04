from django.conf.urls import patterns, url
from problems import views

urlpatterns = patterns(
    '',
    url(r'^get-pending-assignment-list/$', views.PendingAssignmentAPIView.as_view(), name='pending-list'),
    url(r'^get-completed-assignment-list/$', views.CompletedAssignmentAPIView.as_view(), name='completed-list'),
    url(r'^get-problem-list/$', views.ProblemListAPIView.as_view(), name='problem-list'),
)
