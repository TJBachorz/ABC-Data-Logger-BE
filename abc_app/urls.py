from django.urls import path, include
from rest_framework import routers
from .views import LoginView, UserCreateView, AccountView, AccountObjectView, CaseView, CaseLinkView, IncidentView, CaseObjectView

router = routers.DefaultRouter()
router.register('accounts', AccountView)
router.register('accountobjects', AccountObjectView)
router.register('cases', CaseView)
router.register('caseobjects', CaseObjectView)
router.register('caselinks', CaseLinkView)
router.register('incidents', IncidentView)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', UserCreateView.as_view()),
    path('login', LoginView.as_view())
]