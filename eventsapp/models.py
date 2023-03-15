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


class Questions(models.Model):
    description = models.CharField('Описание', max_length=255)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='UserQuestion')
    created_at = models.DateTimeField('Создано', auto_now_add=True)

    def __str__(self):
        return self.description


class Groups(models.Model):
    title = models.CharField('Название', max_length=50)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='GroupUser')
    description = models.CharField('Описание', max_length=255, blank=True)

    def __str__(self):
        return self.title


class Notifications(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='notifications')
    description = models.CharField('Описание', max_length=500, default='')
    is_active = models.BooleanField('Активно', default=False)
    created_at = models.DateTimeField('Создано', auto_now_add=True)


class Notes(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='Notes')
    description = models.CharField('Описание', max_length=500, default='')
    created_at = models.DateTimeField('Создано', auto_now_add=True)

# class Application(models.Model):
#     group = models.ForeignKey('Groups', on_delete=models.CASCADE, related_name='GroupsInvite')
#     recipient = models.TextField('Получатель', max_length=250)
