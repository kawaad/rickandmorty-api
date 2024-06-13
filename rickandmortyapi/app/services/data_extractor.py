import time
from socket import socket

import requests

import sys

sys.path.append('rickandmortyapi')

from app.models import Character, Episode, Location
from requests.exceptions import Timeout

DELAY_REQUESTS = 5


class DataExtractor:
    BASE_URL = "https://rickandmortyapi.com/api/"
    timeout_occurred = False

    def extract_characters(self):
        url = DataExtractor.BASE_URL + "character"
        response = requests.get(url)

        while True:
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
                    character.save()
                    self.update_character_episodes(item, character)
                else:
                    self.update_character_episodes(item, character)
            next_page_url = self.parse_next_page_url(response)
            if next_page_url:
                response = requests.get(next_page_url)
            else:
                break

    @staticmethod
    def update_character_episodes(item, character):
        episode_urls = item['episode']
        episodes = Episode.objects.filter(url__in=episode_urls)
        character.set_episodes(episodes)

    def extract_episodes(self):
        url = DataExtractor.BASE_URL + "episode"
        try:
            if not DataExtractor.timeout_occurred:
                DataExtractor.timeout_occurred = True
                self.simulate_request_timeout()

            response = requests.get(url)

            while True:
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
                        episode.save()
                        self.update_episode_characters(item, episode)
                    else:
                        self.update_episode_characters(item, episode)
                next_page_url = self.parse_next_page_url(response)
                if next_page_url:
                    response = requests.get(next_page_url)
                else:
                    break
        except Timeout:
            raise Timeout("Ocorreu um timeout ao extrair episódios.")

    @staticmethod
    def simulate_request_timeout():
        raise socket.timeout

    @staticmethod
    def update_episode_characters(item, episode):
        character_urls = item['characters']
        characters = Character.objects.filter(url__in=character_urls)
        episode.characters.add(*characters)

    def extract_locations(self):
        url = DataExtractor.BASE_URL + "location"
        response = requests.get(url)

        while True:
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
                    location.save()
                    self.update_location_residents(item, location)
                else:
                    self.update_location_residents(item, location)
            next_page_url = self.parse_next_page_url(response)
            if next_page_url:
                response = requests.get(next_page_url)
            else:
                break

    @staticmethod
    def update_location_residents(item, location):
        character_urls = item['residents']
        characters = Character.objects.filter(url__in=character_urls)
        location.residents.add(*characters)

    @staticmethod
    def parse_next_page_url(response):
        time.sleep(DELAY_REQUESTS)
        next_page_url = response.json().get('info').get('next')
        return next_page_url
