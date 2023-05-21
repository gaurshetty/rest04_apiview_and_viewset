from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', views.TestViewSet, basename='TestViewSet')


urlpatterns = [
    path('apiview/', views.TestAPIView.as_view()),
    path('viewset/', include(router.urls))
]
