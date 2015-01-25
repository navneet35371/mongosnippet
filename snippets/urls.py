from django.conf.urls import url, patterns
from snippets import views

urlpatterns = patterns('',
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippet/(?P<id>[0-9a-z]+)/$', views.SnippetDetail.as_view()),
    
)