from rest_framework import generics
from rest_framework import mixins
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from lists.models import MList
from lists.serializers import MListSerializer,ListSerializer
from rest_framework import permissions
from lists.permissions import IsOwnerOrReadOnly

class MListsView(generics.ListCreateAPIView):
    queryset = MList.objects.all()
    serializer_class = MListSerializer
    def pre_save(self, obj):
    	obj.user = self.request.user


class MListsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MList.objects.all()
    serializer_class = MListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class MListAdd(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            mlist = MList.objects.get(pk=pk)
	    if(mlist.user == self.request.user):
		return mlist
	    else:
        	raise Http404
        except MList.DoesNotExist:
            raise Http404
    def get_movie(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def post(self, request,pk, format=None):
        serializer = ListSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.movie = self.get_movie(request.DATA['movie'])
    	    serializer.mlist = self.get_object(pk)
	    serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



