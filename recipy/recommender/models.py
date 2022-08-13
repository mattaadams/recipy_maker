from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recommender(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # pred = models.CharField(max_length=200)
    # board = ArrayField(
    #     ArrayField(
    #         models.CharField(max_length=10, blank=True),
    #         size=8,
    #     ),
    #     size=8,
    # )

    def __str__(self):
        return f'Recommendations for {self.user}'
