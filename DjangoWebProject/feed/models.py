from django.db import models

class Articles(models.Model):
    img_url = models.URLField(max_length=200)
    title = models.CharField(max_length=100)
    about = models.TextField()
    tag = models.CharField(max_length=50)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    