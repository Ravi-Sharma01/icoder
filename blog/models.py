from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.CharField(max_length=100, default='')
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + " by " + self.author
