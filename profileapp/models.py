from django.db import models

# Create your models here.
class Profile(models.Model):
    title = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body