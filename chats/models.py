from django.contrib.auth.models import User
from django.db import models


class ChatGroup(models.Model):
    group_name = models.CharField(max_length=128, unique=True)
    users_online = models.ManyToManyField(User, related_name='online_in_group', blank=True)

    def __str__(self):
        return self.group_name


class GroupMessages(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} : {self.body}'

    class Meta:
        ordering = ['created']
