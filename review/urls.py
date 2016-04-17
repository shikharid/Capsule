from django.conf.urls import patterns, url
from rest_framework.routers import DefaultRouter
from review import views

router = DefaultRouter()

# Base_name is required as queryset is not set
router.register(r'review', views.ReviewAssignmentViewSet, 'review-assignment')
router.register(r'review/(?P<assignment_id>[\d]+)', views.ReviewStudentViewSet, 'review-student')
urlpatterns = patterns(
    '',
    url(r'^review/assignment-list/$', views.ListAssignmentAPIView.as_view(), name='assignment-list'),
    url(r'^review/(?P<assignment_id>[\d]+)/student-list/$', views.ListStudentAPIView.as_view(), name='student-list')
    )

urlpatterns += router.urls