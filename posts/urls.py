from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views

urlpatterns = [
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^posts/(?P<slug>[-\w]+)/$', views.PostDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
