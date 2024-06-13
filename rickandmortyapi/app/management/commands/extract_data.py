import sys

sys.path.append('rickandmortyapi')

from app.services.data_extractor import DataExtractor
from app.flows.prefect_flows import extract_characters_task, extract_episodes_task, extract_locations_task

from django.core.management.base import BaseCommand
from prefect import flow


class Command(BaseCommand):
    help = 'Fetch data from the Rick and Morty API and store it in the database'

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.SUCCESS('Running prefect flow...'))
        data_extractor = DataExtractor()

        @flow(name="RickAndMortyDataExtraction")
        def extract_flow():
            self.stdout.write(self.style.SUCCESS('Running task and extracting characters...'))
            extract_characters_task(data_extractor)
            self.stdout.write(self.style.SUCCESS('Running task and extracting episodes...'))
            extract_episodes_task(data_extractor)
            self.stdout.write(self.style.SUCCESS('Running task and extracting locations...'))
            extract_locations_task(data_extractor)
            self.stdout.write(self.style.SUCCESS('Flow and data extraction completed!'))

        extract_flow()
