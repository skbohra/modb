from django.contrib import admin
from .models import Movie,Cast,Crew,Revenue

admin.site.register(Movie)
admin.site.register(Cast)
admin.site.register(Crew)
admin.site.register(Revenue)
