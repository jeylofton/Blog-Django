from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(
        max_length=200,
        help_text="Write a description about the status"
    )

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return f"Status: {self.name}"


class Post(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.DO_NOTHING
        )
        

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])
    