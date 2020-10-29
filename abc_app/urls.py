from django.urls import path, include
from rest_framework import routers
from .views import AccountView

router = routers.DefaultRouter()
router.register('accounts', AccountView)

urlpatterns = [
    path('', include(router.urls))
]