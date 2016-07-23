from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aboutme/', hello.views.aboutme, name='aboutme'),
    url(r'^blogs/$', hello.views.blogs, name='blogs'),
    ## eg: /blogs/0
    url(r'^blogs/(?P<blogIndex>[0-9]+)/', hello.views.nblog, name='some_blog'),
)
