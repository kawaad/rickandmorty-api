import requests

import sys

sys.path.append('rickandmortyapi')

from app.models import Character, Episode, Location
from requests.exceptions import Timeout
from django.db import IntegrityError


class DataExtractor:
    BASE_URL = "https://rickandmortyapi.com/api/"

    def extract_characters(self):
        url = DataExtractor.BASE_URL + "character"
        response = requests.get(url)
        data = response.json().get('results', [])
        for item in data:
            origin = Location.objects.filter(url=item.get('origin', {}).get('url')).first()
            location = Location.objects.filter(url=item.get('location', {}).get('url')).first()
            character = Character.objects.filter(source_id=item['id']).first()
            if not character:
                character = Character(
                    name=item['name'],
                    status=item['status'],
                    species=item['species'],
                    type=item['type'],
                    gender=item['gender'],
                    origin=origin,
                    location=location,
                    image=item['image'],
                    source_id=item['id'],
                    url=item['url'],
                    created=item['created']
                )
                import pdb;pdb.set_trace()
                character.save()
                self.update_character_episodes(item, character)
            else:
                self.update_character_episodes(item, character)

    @staticmethod
    def update_character_episodes(item, character):
        episode_urls = item['episode']
        episodes = Episode.objects.filter(url__in=episode_urls)
        character.set_episodes(episodes)

    def extract_episodes(self):
        url = DataExtractor.BASE_URL + "episode"
        try:
            response = requests.get(url, timeout=1)
            response.raise_for_status()
            data = response.json().get('results', [])
            for item in data:
                episode = Episode.objects.filter(source_id=item['id']).first()
                if not episode:
                    episode = Episode(
                        name=item['name'],
                        air_date=item['air_date'],
                        episode=item['episode'],
                        url=item['url'],
                        source_id=item['id'],
                        created=item['created']
                    )
                    import pdb;pdb.set_trace()
                    episode.save()
                    self.update_episode_characters(item, episode)
                else:
                    self.update_episode_characters(item, episode)
        except Timeout:
            raise Timeout("Ocorreu um timeout ao extrair episódios.")

    @staticmethod
    def update_episode_characters(item, episode):
        character_urls = item['characters']
        characters = Character.objects.filter(url__in=character_urls)
        episode.characters.add(*characters)

    def extract_locations(self):
        url = DataExtractor.BASE_URL + "location"
        response = requests.get(url)
        data = response.json().get('results', [])
        for item in data:
            location = Location.objects.filter(source_id=item['id']).first()
            if not location:
                location = Location(
                    name=item['name'],
                    type=item['type'],
                    dimension=item['dimension'],
                    url=item['url'],
                    source_id=item['id'],
                    created=item['created']
                )
                import pdb;pdb.set_trace()
                location.save()
                self.update_location_residents(item, location)
            else:
                self.update_location_residents(item, location)

    @staticmethod
    def update_location_residents(item, location):
        character_urls = item['residents']
        characters = Character.objects.filter(url__in=character_urls)
        location.residents.add(*characters)

