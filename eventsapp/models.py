from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Event(models.Model):
    title = models.CharField('Название', max_length=30)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='UserEvents')
    description = models.CharField('Описание', max_length=500)
    is_active = models.BooleanField('Активно', default=False)
    is_deleted = models.BooleanField('Удалено', default=False)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    chose_date = models.TextField('Запланировано', default='')

    def __str__(self):
        return self.title


class CustomUser(models.Model):
    full_name = models.CharField('Фамилия_Имя', max_length=255, default='')
    created_at = models.DateTimeField('Создано', auto_now=True)
    telegram_id = models.PositiveIntegerField('Телеграм ID', unique=True)
    username = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.full_name
