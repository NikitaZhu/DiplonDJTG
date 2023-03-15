from rest_framework import serializers

from eventsapp.models import CustomUser, Event, Questions, Groups, Notifications


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        read_only_fields = ['id', ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ['id', ]
        date = serializers.DateField(input_formats=['%d-%m-%Y', ])


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
        read_only_fields = ['id', ]


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'
        read_only_fields = ['id', ]


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'
        read_only_fields = ['id']
