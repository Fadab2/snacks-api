from ssl import create_default_context
from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    title = models.CharField(max_length=100)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
