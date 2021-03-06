from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = (
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aboutme/', hello.views.aboutme, name='aboutme'),
    url(r'^books/bookclub/$', hello.views.bookclub, name='bookclub'),
    url(r'^books/$', hello.views.books, name='books'),
    url(r'^blogs/$', hello.views.blogs, name='blogs'),
    ## eg: /blogs/0
    url(r'^blogs/(?P<blogIndex>[0-9]+)/', hello.views.nblog, name='some_blog'),
)
