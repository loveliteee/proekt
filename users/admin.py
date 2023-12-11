from django.contrib import admin
from django.db import models
from users import models

# Register your models here.
admin.site.register(models.User)
