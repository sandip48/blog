from django.db import models

from accounts.models import User
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