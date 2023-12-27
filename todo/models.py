from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    CURRENT = 'current'
    COMPLETED = 'completed'

    STATUS_CHOICES = [
        (CURRENT, 'Current'),
        (COMPLETED, 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    memo = models.TextField()
    # completed = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=CURRENT,
    )

    def __str__(self):
        return self.title
