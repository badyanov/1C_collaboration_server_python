from .models import Group, Channel, Message, Log
from django.views.generic import ListView, DetailView

class Index(ListView):
    model = Log
    paginate_by: int = 10
    template_name: str = 'cs/index.html'

class GroupList(ListView):
    model = Group

class GroupPost(DetailView):
    model = Group

class ChannelList(ListView):
    model = Channel

class ChannelPost(DetailView):
    model = Channel

class MessageList(ListView):
    model = Message

class MessagePost(DetailView):
    model = Message