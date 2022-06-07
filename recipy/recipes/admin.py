from django.contrib import admin
# Register your models here.
from .models import Recipe, Comment

admin.site.register(Recipe)
admin.site.register(Comment)
