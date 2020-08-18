from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='csv')

    def __str__(self):
        return self.title