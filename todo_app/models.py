from django.db import models

# Create your models here.
class To_Do(models.Model):
    text = models.CharField(max_length=200)
    added_date = models.DateTimeField()

    def __str__(self):
        return self.text