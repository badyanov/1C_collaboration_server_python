from email import message
import imp
from statistics import mode
from django.db import models
from datetime import datetime
from django.conf import settings

class Group(models.Model):
    name = models.CharField(max_length=200, verbose_name='Группа')

    def __str__(self) -> str:
        return self.name

    @classmethod
    def channel_name(cls, group_id):
        return 'group_{}'.format(group_id)


class Channel(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='channel_group', verbose_name='Группа', null=True)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='channel_user', verbose_name='Пользователь', null=True)

    def __str__(self) -> str:
        return self.user.name


class Message(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='message_group', verbose_name='Группа', null=True)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='message_user', verbose_name='Пользователь', null=True)    

    message = models.TextField(verbose_name='Сообщение')

    def __str__(self) -> str:
        return self.message

    
class Log(models.Model):
    ERROR = 'E'
    INFO = 'i'
    LOG_STATUS = [
        (ERROR, 'Ошибка'),
        (INFO, 'Информация')
    ]
    log_type = models.CharField(max_length=1, verbose_name='Тип сообщения', choices=LOG_STATUS, default=INFO)
    text = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(verbose_name='Дата', default=datetime.now)

    def __str__(self) -> str:
        return 'Тип: {}, Сообщение: {}'.format(self.log_type, self.text)
    
    class Meta:
        ordering = ['-date']
