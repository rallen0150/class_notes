from django.contrib import admin
from app.models import Batting, Pitching

# Register your models here.
admin.site.register([Batting, Pitching])
