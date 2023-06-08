from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings


def validation_content(value):  # Content Validation
    content = value
    if content == "abc":
        raise ValidationError("Cannot be ABC")
    return value


class Tweet (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140, validators=[validation_content])
    updated = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)
