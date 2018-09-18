from django.urls import include, path

from apps.core import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls'), name='rest_login'),
    path('rest-auth/', include('rest_auth.urls'), name='rest_login'),
    path('rest-auth/facebook', views.FacebookLogin.as_view(), name='rest_login_facebook'),
    path('rest-auth/google', views.GoogleLogin.as_view(), name='rest_login_google'),
    path('rest-auth/google', views.TwitterLogin.as_view(), name='rest_login_twitter'),
    path('rest-auth/google', views.LinkedinLogin.as_view(), name='rest_login_linkedin'),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    ]
