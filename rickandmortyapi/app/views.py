from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import IntegrityError

from .models import Episode, Location, Character
from .serializers import EpisodeSerializer, LocationSerializer, CharacterSerializer


# Create your views here.
class EpisodeListAPIView(APIView):

    @staticmethod
    def get(request):
        episodes = Episode.objects.all()
        serializer = EpisodeSerializer(episodes, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = EpisodeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                episode = serializer.save()
                character_urls = request.data.get('characters', [])
                characters = Character.objects.filter(url__in=character_urls)
                episode.characters.set(characters)
                episode.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"error": "An episode with this source_id already exists."},
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EpisodeAPIView(APIView):

    @staticmethod
    def get_object(source_id):
        try:
            return Episode.objects.get(source_id=source_id)
        except Episode.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, source_id):
        episode = self.get_object(source_id)
        if isinstance(episode, Response):
            return episode

        serializer = EpisodeSerializer(episode)
        return Response(serializer.data)

    def put(self, request, source_id):
        episode = self.get_object(source_id)
        if isinstance(episode, Response):
            return episode

        serializer = EpisodeSerializer(episode, data=request.data)
        if serializer.is_valid():
            episode = serializer.save()
            character_urls = request.data.get('characters', [])
            characters = Character.objects.filter(url__in=character_urls)
            episode.characters.set(characters)
            episode.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, source_id):
        episode = self.get_object(source_id)
        if isinstance(episode, Response):
            return episode

        episode.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LocationListAPIView(APIView):

    @staticmethod
    def get(request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                location = serializer.save()
                residents_urls = request.data.get('residents', [])
                residents = Character.objects.filter(url__in=residents_urls)
                location.residents.set(residents)
                location.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"error": "A location with this source_id already exists."},
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationAPIView(APIView):

    @staticmethod
    def get_object(source_id):
        try:
            return Location.objects.get(source_id=source_id)
        except Location.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, source_id):
        location = self.get_object(source_id)
        if isinstance(location, Response):
            return location

        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, source_id):
        location = self.get_object(source_id)
        if isinstance(location, Response):
            return location

        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            location = serializer.save()
            residents_urls = request.data.get('residents', [])
            residents = Character.objects.filter(url__in=residents_urls)
            location.residents.set(residents)
            location.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, source_id):
        location = self.get_object(source_id)
        if isinstance(location, Response):
            return location

        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CharacterListAPIView(APIView):

    @staticmethod
    def get(request):
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"error": "A character with this source_id already exists."},
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CharacterAPIView(APIView):

    @staticmethod
    def get_object(source_id):
        try:
            return Character.objects.get(source_id=source_id)
        except Character.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, source_id):
        character = self.get_object(source_id)
        if isinstance(character, Response):
            return character

        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    def put(self, request, source_id):
        character = self.get_object(source_id)
        if isinstance(character, Response):
            return character

        serializer = CharacterSerializer(character, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, source_id):
        character = self.get_object(source_id)
        if isinstance(character, Response):
            return character

        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
