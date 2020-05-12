from django.contrib.auth.models import AbstractUser
from django.db import models


class EventUser(AbstractUser):
    is_troupe_leader = models.BooleanField(default=False)
    is_clown = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Troupe(models.Model):
    name = models.CharField(max_length=50)
    leader = models.ForeignKey(EventUser, on_delete=models.CASCADE, related_name='leader')
    strength = models.IntegerField()
    clown = models.ManyToManyField(EventUser, related_name='clown')

    def __str__(self):
        return self.name



class Event(models.Model):
    UPCOMING = 'upcoming'
    INCIPIENT = 'incipient'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    STATUS = [
        (UPCOMING, ('Upcoming')),
        (INCIPIENT,('Incipient')),
        (COMPLETED,('Completed')),
        (CANCELLED,('Cancelled')),
    ]
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default=None,
    )
    EXCELLENT = 'excellent'
    GOOD = 'good'
    BAD = 'bad'
    VERYBAD = 'very bad'

    RATING = [
        (EXCELLENT, ('Excellent')),
        (GOOD, ('Good')),
        (BAD, ('Bad')),
        (VERYBAD, ('Very bad')),
    ]
    rating = models.CharField(
        max_length=32,
        choices=RATING,
        default=None,
    )
    name = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    issues = models.CharField(max_length=200, blank=True)
    troupe = models.ForeignKey(Troupe, on_delete=models.CASCADE, related_name='troupe1')
    client = models.ForeignKey(EventUser, on_delete=models.CASCADE, related_name='client1')

    def __str__(self):
        return self.name
