from django.forms import widgets
from rest_framework import serializers
from .models import ListItem,MList


class MListSerializer(serializers.ModelSerializer):
	class Meta:
        	model = MList
   	mlist= serializers.RelatedField(many=True)
	user = serializers.Field(source='user.username')

class ListSerializer(serializers.ModelSerializer):
	class Meta:
        	model = ListItem
		fields = ('id','mlist',)
