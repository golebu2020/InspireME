from django.contrib import admin

# Register your models here.
from .models import Profile, Category, Post, Like

models = [Profile, Category, Post, Like]

for model in models:
  admin.site.register(model)

