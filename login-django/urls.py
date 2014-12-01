from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'login_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'login_django.views.login_page', name='login'),
    url(r'^$', 'login_django.views.homepage', name='homepage'),
    url(r'^logout/$', 'login_django.views.logout_view', name='logout'),
)
