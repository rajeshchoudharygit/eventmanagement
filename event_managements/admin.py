from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import EventUserCreationForm, EventUserChangeForm
from .models import EventUser, Troupe, Event

class EventUserAdmin(UserAdmin):
    add_form = EventUserCreationForm
    form = EventUserChangeForm
    model = EventUser
    list_display = ['email', 'username',]

admin.site.register(EventUser, EventUserAdmin)
admin.site.register(Troupe)
admin.site.register(Event)