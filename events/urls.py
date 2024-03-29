"""events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from eventsapp.views import EventViewSet, CustomUserViewSet, TgIdListView, UserEventsList, QuestionsViewSet, \
    GroupsViewSet, NotificationsViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'questions', QuestionsViewSet, basename='questions')
router.register(r'groups', GroupsViewSet, basename='groups')
router.register(r'notifications', NotificationsViewSet, basename='notifications')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('telegram_id/', TgIdListView.as_view()),
    path('eventsuser/', UserEventsList.as_view())
]
