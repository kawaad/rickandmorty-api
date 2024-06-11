from rest_framework import serializers

from .models import Episode, Location, Character


class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Episode
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Location
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:

        model = Character
        fields = '__all__'
