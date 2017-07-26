from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models
from datetime import datetime


# Create your models here.
class TripManager(models.Manager):
    def tripVal(self, postData):
        results = {
            'status': True,
            'errors': []
        }
        if not postData['destination']:
            results['status'] = False
            results['errors'].append('Please enter a destination.')
        if not postData['description']:
            results['status'] = False
            results['errors'].append('Please enter a description.')
        if not postData['start_date'] or datetime.strptime(postData['start_date'], "%Y-%m-%d") < datetime.now():
            results['status'] = False
            results['errors'].append('Please enter a future start date.')
        if not postData['end_date'] or postData['end_date'] < postData['start_date']:
            results['status'] = False
            results['errors'].append('Please enter an end date that comes after the start date.')
        return results

    def createTrip(self, postData):
        trip = Trip.objects.create(destination = postData['destination'], description=postData['description'], start_date=postData['start_date'], end_date=postData['end_date'], planned_by=User.objects.get(id=postData['planned_by']))
        return trip


class Trip(models.Model):
    destination = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    start_date = models.DateField()
    end_date = models.DateField()
    planned_by = models.ForeignKey(User, related_name = 'first_user')
    users_joined = models.ManyToManyField(User, related_name = 'joined_users')
    objects = TripManager()
