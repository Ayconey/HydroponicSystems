from rest_framework.authtoken.views import ObtainAuthToken
from django.urls import path

urlpatterns = [
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),
]