from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .serializers.serializers import CustomUserSerializer, EventSerializer

from .models import CustomUser, Event


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('full_name')
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.dict()
        telegram_id = int(data.pop("telegram_id"))
        user, _ = CustomUser.objects.get_or_create(**data, telegram_id=telegram_id)
        return Response(self.serializer_class(user).data)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


