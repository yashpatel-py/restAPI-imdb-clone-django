from django.db import models

class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title