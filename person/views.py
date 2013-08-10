from .models import Person
from .serializers import PersonSerializer
from rest_framework import generics
from mediacontent.models import Album,Image
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from mediacontent.serializers import ImageSerializer
from lists.models import ListItem
from lists.serializers import ListSerializer

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonImageList(APIView):
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
	albums = Album.objects.filter(person=self.get_object(pk))
        images = Image.objects.filter(Q(movies_linked__in=[self.get_object(pk=pk),]) | Q(album=albums))
        serializer = ImageSerializer(images)
        return Response(serializer.data)

    def post(self, request,pk, format=None):
        serializer = ImageSerializer(data=request.DATA)
        if serializer.is_valid():
	    serializer.person_linked = self.get_object(pk)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonVideoList(APIView):
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
	channels = VideoChannel.objects.filter(person=self.get_object(pk))
        videos = Video.objects.filter(Q(movies_linked__in=[self.get_object(pk=pk),]) | Q(channel=channels))
        serializer = VideoSerializer(videos)
        return Response(serializer.data)

    def post(self, request,pk, format=None):
        serializer = VideoSerializer(data=request.DATA)
        if serializer.is_valid(): 
            serializer.person_linked = [self.get_object(pk),]
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonRelatedLists(APIView):
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
	tags = ListItem.objects.filter(person=self.get_object(pk))
        serializer = ListSerializer(tags)
        return Response(serializer.data)




