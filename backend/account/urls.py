from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetail, UserMe, AuthLogin

urlpatterns = [
    url(r'^users/?$', UserList.as_view()),
    url(r'^users/me/?$', UserMe.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/?$', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
