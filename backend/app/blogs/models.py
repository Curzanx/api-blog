from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
