from django import forms
from main import models
from main.models import Product
from django.db import models
from django.contrib.postgres.fields import ArrayField


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

