# Create your views here.
from movie.models import Movie,Cast,Crew,Revenue,ReleaseDate
from movie.serializers import * 
from rest_framework import generics
from rest_framework import mixins
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mediacontent.models import Album,Image,VideoChannel,Video
from mediacontent.serializers import *
from django.db.models import Q

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

'''
#TODO - POST method needs to be tested and fixed
'''
class ProductionCompanies(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
	tags = Tag.objects.filter(movie=self.get_object(pk))
        serializer = ProductionCompaniesSerializer(tags)
        return Response(serializer.data)

    def post(self, request,pk, format=None):
        serializer = ProductionCompaniesSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.movie = self.get_object(pk)
     	    serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieRelatedLists(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
	tags = ListItem.objects.filter(movie=self.get_object(pk))
        serializer = ListSerializer(tags)
        return Response(serializer.data)




class CastList(APIView):

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cast = Cast.objects.filter(movie=self.get_object(pk))
        serializer = CastSerializer(cast)
        return Response(serializer.data)

    def post(self, request,pk, format=None):
        serializer = CastSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.movie = self.get_object(pk)
     	    serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CastDetail(APIView):

    def get_cast_object(self,pk):
	try:
		return Cast.objects.get(pk=pk)
	except Cast.DoesNotExist:
		raise Http404
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id,pk, format=None):
        cast = self.get_cast_object(pk)
	serializer = CastSerializer(cast)
        return Response(serializer.data)

    def put(self, request, id,pk, format=None):
	cast = self.get_cast_object(pk)
        serializer = CastSerializer(cast, data=request.DATA)
        if serializer.is_valid():
            serializer.movie = self.get_object(pk)
	    serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,id, pk, format=None):
	cast = self.get_cast_object(pk)
	cast.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class CrewList(APIView):

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        crew = Crew.objects.filter(movie=self.get_object(pk))
        serializer = CrewSerializer(crew)
        return Response(serializer.data)

    def post(self, request,pk, format=None):
        serializer = CrewSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.movie = self.get_object(pk)
	    serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CrewDetail(APIView):

    def get_crew_object(self,pk):
	try:
		return Crew.objects.get(pk=pk)
	except Crew.DoesNotExist:
		raise Http404
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id,pk, format=None):
        crew = self.get_crew_object(pk)
	serializer = CrewSerializer(crew)
        return Response(serializer.data)

    def put(self, request, id,pk, format=None):
	crew = self.get_crew_object(pk)
        serializer = CrewSerializer(crew, data=request.DATA)
        if serializer.is_valid():
            serializer.movie = self.get_object(pk)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,id, pk, format=None):
	crew = self.get_crew_object(pk)
	crew.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 



class ReleaseList(APIView):

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        releases = ReleaseDate.objects.filter(movie=self.get_object(pk))
        serializer = ReleaseDateSerializer(releases)
        return Response(serializer.data)

    def post(self, request,pk, format=None):
        serializer = ReleaseDateSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.movie = self.get_object(pk)
	    serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RevenueList(APIView):

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        revenue = Revenue.objects.filter(movie=self.get_object(pk))
        serializer = RevenueSerializer(revenue)
        return Response(serializer.data)

    def post(self, request,pk, format=None):
        serializer = RevenueSerializer(data=request.DATA)
        if serializer.is_valid():
	    serializer.movie = self.get_object(pk)
	    serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageTypesList(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk,type, format=None):
	albums = Album.objects.filter(movie=self.get_object(pk))
        images = Image.objects.filter(Q(movies_linked__in=[self.get_object(pk=pk),]) | Q(album=albums)).filter(type=type)
        serializer = ImageSerializer(images)
        return Response(serializer.data)

    def post(self, request,pk,type, format=None):
        serializer = ImageSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageList(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
	albums = Album.objects.filter(movie=self.get_object(pk))
        images = Image.objects.filter(Q(movies_linked__in=[self.get_object(pk=pk),]) | Q(album=albums))
        serializer = ImageSerializer(images)
        return Response(serializer.data)

    def post(self, request,pk, format=None):
        serializer = ImageSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoTypesList(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, type,format=None):
	channels = VideoChannel.objects.filter(movie=self.get_object(pk))
        videos = Video.objects.filter(Q(movies_linked__in=[self.get_object(pk=pk),]) | Q(channel=channels)).filter(type=type)
        serializer = VideoSerializer(videos)
        return Response(serializer.data)

    def post(self, request,pk,type, format=None):
        serializer = VideoSerializer(data=request.DATA)
        if serializer.is_valid(): 
            serializer.movies_linked = [self.get_object(pk),]
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoList(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
	channels = VideoChannel.objects.filter(movie=self.get_object(pk))
        videos = Video.objects.filter(Q(movies_linked__in=[self.get_object(pk=pk),]) | Q(channel=channels))
        serializer = VideoSerializer(videos)
        return Response(serializer.data)

    def post(self, request,pk, format=None):
        serializer = VideoSerializer(data=request.DATA)
        if serializer.is_valid(): 
            serializer.movies_linked = [self.get_object(pk),]
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
