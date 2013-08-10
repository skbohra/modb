from django.forms import widgets
from rest_framework import serializers
from movie.models import Movie,Cast,Crew,Revenue,ReleaseDate
from mediacontent.models import Album,VideoChannel
from taggit.models import Tag,TaggedItemBase
from mediacontent.serializers import AlbumSerializer
from lists.models import ListItem
from lists.serializers import ListSerializer

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('name',)

class TaggedObjectRelatedField(serializers.RelatedField):
        
	def to_native(self, value): 
        	if isinstance(value, Tag):
            		serializer = TagSerializer(value)
        	else:
            		raise Exception('Unexpected type of tagged object')
        	return serializer.data

class AlbumRelatedField(serializers.RelatedField):
        
	def to_native(self, value): 
        	if isinstance(value, Album):
            		serializer = AlbumSerializer(value)
        	else:
            		raise Exception('Unexpected type of object')
        	return serializer.data

class ListRelatedField(serializers.RelatedField):
        
	def to_native(self, value): 
        	if isinstance(value, ListItem):
            		serializer = ListSerializer(value)
        	else:
            		raise Exception('Unexpected type of object')
        	return serializer.data

class MovieSerializer(serializers.ModelSerializer):
    	cast = serializers.RelatedField(many=True)
    	crew = serializers.RelatedField(many=True)
   	revenue = serializers.RelatedField(many=True)
   	release_date= serializers.RelatedField(many=True)
	genres = TaggedObjectRelatedField(many=True)
	keywords = TaggedObjectRelatedField(many=True)
	languages = TaggedObjectRelatedField(many=True)
	production_companies = TaggedObjectRelatedField(many=True)
	albums = AlbumRelatedField(many=True)	
	mlists = ListRelatedField(many=True)
	class Meta:
        	model = Movie

class ProductionCompaniesSerializer(serializers.ModelSerializer):
	class Meta:
        	model = Tag
		fields = ('id','name')

class CastSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cast

class CrewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Crew

class RevenueSerializer(serializers.ModelSerializer):
	class Meta:
		model = Revenue

class ReleaseDateSerializer(serializers.ModelSerializer):
	class Meta:
		model = ReleaseDate

		
