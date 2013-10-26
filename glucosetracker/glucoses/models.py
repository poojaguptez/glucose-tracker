from django.db import models
from django.contrib.auth.models import User

from core.models import TimeStampedModel


class Glucose(TimeStampedModel):
    class Meta:
        ordering = ['-record_date', '-record_time']
    user = models.ForeignKey(User)
    value = models.IntegerField()
    category = models.ForeignKey('Category')
    record_date = models.DateField('Date')
    record_time = models.TimeField('Time')
    notes = models.TextField('Notes', blank=True, default='')

    def __unicode__(self):
        return str(self.value)


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['id']
    name = models.CharField(unique=True, max_length=255)

    def __unicode__(self):
        return self.name
