from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from BlogApp import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mongosnippet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('snippets.urls')),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<id>[\w]{24})/$', views.UserDetails.as_view()),
    url(r'^blogs/$', views.BlogList.as_view()),
    url(r'^blogs/(?P<id>[\w]{24})/$', views.BlogDetails.as_view()),
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^posts/(?P<id>[\w]{24})/$', views.PostDetails.as_view()),
    url(r'^comments/$', views.CommentList.as_view()),
    url(r'^comments/(?P<id>[\w]{24})/$', views.CommentDetails.as_view()),
)
urlpatterns = format_suffix_patterns(urlpatterns)