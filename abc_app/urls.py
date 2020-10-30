from django.urls import path, include
from rest_framework import routers
from .views import AccountView, CaseView, CaseLinkView

router = routers.DefaultRouter()
router.register('accounts', AccountView)
router.register('Cases', CaseView)
router.register('CaseLink', CaseLinkView)

urlpatterns = [
    path('', include(router.urls))
]