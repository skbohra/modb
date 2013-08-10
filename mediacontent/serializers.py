from django.forms import widgets
from rest_framework import serializers
from .models import Album,Image,Video


class AlbumSerializer(serializers.ModelSerializer):
	class Meta:
		model = Album
    	
	image = serializers.RelatedField(many=True)

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video 
    	
