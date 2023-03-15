from django.contrib import admin
from .models import Event, CustomUser, Questions, Groups, Notifications


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'updated_at',
        'created_at',
        'is_active',
        'is_deleted',
        'user',
    ]
    search_fields = ['title']


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = [
        'id',
        'full_name',
        'telegram_id'
    ]
    search_fields = [
        'full_name',
        'telegram_id',
    ]


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'description',
        'user'
    ]


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description'
    ]


@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'description',
        'created_at'
    ]