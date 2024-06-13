from rest_framework import serializers

from .models import Episode, Location, Character


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:

        model = Character
        fields = '__all__'


class EpisodeSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True, required=False)

    class Meta:

        model = Episode
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    residents = CharacterSerializer(many=True, required=False)

    class Meta:

        model = Location
        fields = '__all__'
