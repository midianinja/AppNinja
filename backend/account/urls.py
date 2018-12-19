from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetail, UserMe, Cadastro


urlpatterns = [
    url(r'^users/?$', UserList.as_view()),
    url(r'^users/confirm/(?P<user_id>.*)/(?P<token>.*)$', UserList.email_verification),
    url(r'^users/send-recover/?$', UserList.send_recover_password),
    url(r'^users/recover/(?P<user_id>.*)/(?P<token>.*)?$', UserList.recover_password),
    url(r'^users/skills/?$', UserList.list_skills),
    url(r'^users/causes/?$', UserList.list_causes),
    url(r'^users/interests/?$', UserList.list_interests),
    url(r'^users/me/?$', UserMe.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/?$', UserDetail.as_view()),
    url(r'^cadastro/', Cadastro.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
