from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    datestamp = models.DateField()
    blogentry = models.TextField()

    def __str__(self):
        return self.title + " - " + self.datestamp.strftime('%Y-%m-%d')
