import sys
import os

sys.path.append('rickandmortyapi')

from app.services.data_extractor import DataExtractor
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Fetch data from the Rick and Morty API and store it in the database'

    def handle(self, *args, **kwargs):
        data_extractor = DataExtractor()
        # self.stdout.write(self.style.SUCCESS('Extracting characters...'))
        # data_extractor.extract_characters()
        # self.stdout.write(self.style.SUCCESS('Extracting episodes...'))
        # data_extractor.extract_episodes()
        # self.stdout.write(self.style.SUCCESS('Extracting locations...'))
        data_extractor.extract_locations()
        self.stdout.write(self.style.SUCCESS('Data extraction completed!'))
