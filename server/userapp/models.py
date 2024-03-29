from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
