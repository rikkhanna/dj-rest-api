from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, basename='hello-viewset')


urlpatterns = [
    path('hello-view/',views.HelloApi.as_view()),
    path('', include(router.urls))
]
