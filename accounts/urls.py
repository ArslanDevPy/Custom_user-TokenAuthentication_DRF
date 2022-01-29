from django.urls import path
from rest_framework import routers
from accounts.views import UserModeViewSet

router = routers.DefaultRouter()
router.register('users', UserModeViewSet)
urlpatterns = router.urls
