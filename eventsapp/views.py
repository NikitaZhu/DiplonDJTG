from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .serializers.serializers import CustomUserSerializer, EventSerializer, QuestionsSerializer, GroupsSerializer, \
    NotificationsSerializer

from .models import CustomUser, Event, Questions, Groups, Notifications


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['telegram_id']
    pagination_class = LimitOffsetPagination

    def create(self, request, *args, **kwargs):
        data = request.data.dict()
        telegram_id = int(data.pop("telegram_id"))
        user, _ = CustomUser.objects.get_or_create(**data, telegram_id=telegram_id)
        return Response(self.serializer_class(user).data)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'title']

    # def create(self, request, *args, **kwargs):
    #     data = request.data.dict()
    #     telegram_id = int(data.pop("telegram_id"))
    #     user, _ = Event.objects.get_or_create(**data, telegram_id=telegram_id)
    #     return Response(self.serializer_class(user).data)


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'description']


class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'description']

class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'title']


class TgIdListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['telegram_id']


class UserEventsList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user']
    pagination_class = LimitOffsetPagination
