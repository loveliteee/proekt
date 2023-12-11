from django.contrib import admin
from django.db import models
from main import models

admin.site.register(models.ProductCategory)

admin.site.register(models.Product)

admin.site.register(models.Feature)

