from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from .validators import validate_file_extension,file_size

class Recipe(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(default='default_food.png', upload_to='recipe_pics',validators=[validate_file_extension,file_size])
    # Slug
    image_url = models.URLField(max_length=300, null=True, blank=True)
    description = models.TextField()
    instructions = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, related_name='favorites', default=None, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipe-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="ingredients", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Comment(models.Model):
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE, default=1)
    recipe = models.ForeignKey(Recipe, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f"{self.recipe} - {self.id} - {self.author}"
