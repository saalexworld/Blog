from django.urls import path
from rest_framework import routers

from .views import PostViewSet, CategoryViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('category', CategoryViewSet)


urlpatterns = []
urlpatterns += router.urls