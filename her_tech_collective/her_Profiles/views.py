from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HerProfile, Location
from .serializers import HerProfileSerializer, LocationSerializer
from django.http import Http404
from rest_framework import status, permissions


class HerProfileList(APIView):

    def get(self, request):
        her_profile = HerProfile.objects.all()
        serializer = HerProfileSerializer(her_profile, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = HerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    


class HerProfileDetail(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            her_profile = HerProfile.objects.get(pk=pk)
            self.check_object_permissions(self.request, her_profile)
            return her_profile

        except HerProfile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        her_profile = self.get_object(pk)
        serializer = HerProfileSerializer(her_profile)
        return Response(serializer.data)
    
    def put(self, request, pk):
        her_profile = self.get_object(pk)
        serializer = HerProfileSerializer(
            instance=her_profile,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        her_profile = self.get_object(pk)
        her_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class LocationList(APIView):

    def get(self, request):
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)
        return Response(serializer.data)