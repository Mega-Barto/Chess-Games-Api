from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (ListResultsView)
from .viewsets import (GameViewSet, PlayerViewSet)

router = DefaultRouter()
router.register('games', GameViewSet)
router.register('players', PlayerViewSet)

urlpatterns = [
    path('results/', ListResultsView.as_view()),
] + router.urls
