from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetail, UserMe, AuthLogin, Cadastro
from . import views
#import ipdb; ipdb.set_trace()

urlpatterns = [
    url(r'^users/?$', UserList.as_view()),
    url(r'^users/confirm/(?P<user_id>.*)/(?P<token>.*)$', UserList.email_verification),
    url(r'^users/me/?$', UserMe.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/?$', UserDetail.as_view()),
    url(r'^cadastro/', Cadastro.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
