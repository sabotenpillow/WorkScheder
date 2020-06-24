from django.db import models
#from django.contrib.auth.models import User
from accounts.models import User

# Create your models here.

class WorkSchedule(models.Model):
    date = \
        models.DateField(
            verbose_name = 'date',
            auto_now_add = False
        )
    work_schedule = \
        models.CharField(
            verbose_name = 'work sched',
            max_length   = 5,
            null         = False,
            blank        = False
        )
    user = \
        models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Workschedule'

    def __str__(self):
        return str(self.date)
