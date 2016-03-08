from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from authentication import urls as auth_urls
from problems import urls as problem_urls

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
from webapp.settings import MEDIA_URL, MEDIA_ROOT

admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns(
    '',
    # Admin panel and documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/user/', include(auth_urls)),
    url(r'^api/problem/', include(problem_urls)),
    url('^.*$', TemplateView.as_view(template_name='index.html'), name="index"),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
