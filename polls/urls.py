from django.urls import path
from rest_framework.authtoken import views as auth_views


from . import views

urlpatterns = [
    path("", views.UserListAPIView.as_view(), name="index"),
    path("sign-up/", views.UserCreateAPIView.as_view(), name="index"),
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),

]