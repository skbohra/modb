from django.contrib import admin
from .models import Video,Image,VideoChannel,Album

admin.site.register(Video)
admin.site.register(VideoChannel)
admin.site.register(Image)
admin.site.register(Album)
