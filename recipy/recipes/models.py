from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipe-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="comments", on_delete=models.CASCADE)
    #author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.recipe.title} - {self.name}"
