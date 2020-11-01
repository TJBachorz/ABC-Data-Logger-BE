from django.urls import path, include
from rest_framework import routers
from .views import AccountView, CaseView, CaseLinkView, IncidentView

router = routers.DefaultRouter()
router.register('accounts', AccountView)
router.register('cases', CaseView)
router.register('caselinks', CaseLinkView)
router.register('incidents', IncidentView)

urlpatterns = [
    path('', include(router.urls))
]