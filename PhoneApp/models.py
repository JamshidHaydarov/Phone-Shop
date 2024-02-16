from django.db import models

class Phone(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    body = models.CharField(db_column='body', max_length=100, blank=False)
    characteristics = models.TextField(db_column='characteristics', max_length=250, blank=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

# Create your models here.
