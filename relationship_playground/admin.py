from django.contrib import admin
from relationship_playground import models

# Register your models here.
admin.site.register(
    [
        models.Articles,
        models.Author,
        models.Topping,
        models.Pizza,
        models.Person,
        models.Society,
        models.Membership
    ]
)
