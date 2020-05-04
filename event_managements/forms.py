from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import EventUser


class EventUserCreationForm(UserCreationForm):

    class Meta:
        model = EventUser
        fields = ('username', 'email', 'is_troupe_leader', 'is_clown', 'is_client')

class EventUserChangeForm(UserChangeForm):

    class Meta:
        model = EventUser
        fields = ('username', 'email', 'is_troupe_leader', 'is_clown', 'is_client')