from django.db import models

# Create your models here.

class WorkPatterns(models.Model):
    pattern = \
        models.CharField(
            verbose_name = 'work pattern',
            max_length   = 100,
            null         = False,
            blank        = False
        )

    class Meta:
        verbose_name_plural = 'WorkPatterns'

    def __str__(self):
        return self.pattern
