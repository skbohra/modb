from django.forms import widgets
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
        	model = Person
		
