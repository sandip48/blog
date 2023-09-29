from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_query_name="post")
    title=models.CharField(max_length=200)
    content=models.TextField()
    active=models.BooleanField(default=True)
    image=models.ImageField(upload_to="post/",null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.title