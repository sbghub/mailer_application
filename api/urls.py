from rest_framework.authtoken.views import obtain_auth_token

urlpatterns += [ url(r'^obtain-auth-token/$', obtain_auth_token) ]