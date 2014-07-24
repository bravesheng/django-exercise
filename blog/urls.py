from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.home'),
    url(r'^article/(?P<pk>[0-9]+)/$', 'article.views.detail'),
    url(r'^create/$', 'article.views.create'),
    url(r'^time/$', 'article.views.current_datetime'),
    url(r'^another-time-page/$', 'article.views.current_datetime'),
    (r'^time/plus/(\d{1,2})/$', 'article.views.hours_ahead'),
)
