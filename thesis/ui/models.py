from django.db import models

class csvFile(models.Model):
    title = models.CharField(max_length=200)
    csv = models.FileField(upload_to='csv')

    def __str__(self):
        return self.title