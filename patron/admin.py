from django.contrib import admin
from .models import MissingPerson, Gender, State, Race

# Register your models here.
admin.site.register(MissingPerson)
admin.site.register(Gender)
admin.site.register(Race)
admin.site.register(State)