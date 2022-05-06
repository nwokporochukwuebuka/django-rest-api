from rest_framework.routers import DefaultRouter
from django.urls import path, include 
from .views import EventMainView

router = DefaultRouter()
router.register("event", EventMainView)

urlpatterns = [
    path("", include(router.urls))
]