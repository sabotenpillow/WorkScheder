from django.db import models

# Create your models here.

class WorkSchedule(models.Model):
    date = \
        models.DateField(
            verbose_name = '年月日',
            auto_now_add = False,
            unique       = True
        )
    work_schedule = \
        models.CharField(
            verbose_name = '勤務日程',
            max_length   = 5,
            null         = False,
            blank        = False
        )

    class Meta:
        verbose_name_plural = 'Workschedule'

    def __str__(self):
        return str(self.date)
