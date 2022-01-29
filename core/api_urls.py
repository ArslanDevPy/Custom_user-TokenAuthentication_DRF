from django.urls import path, include
from accounts.views import ObtainAuthToken

urlpatterns = [
    path('token/', ObtainAuthToken.as_view(), name='token'),
    path('accounts/', include('accounts.urls')),
]
