from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, ListingViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'listings', ListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
