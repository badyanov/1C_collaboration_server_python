from django.contrib import admin
from .models import Group, Channel, Message, Log

admin.site.register(Group)
admin.site.register(Channel)
admin.site.register(Message)
admin.site.register(Log)
