from django.db import models
from django.contrib.auth.models import User
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
