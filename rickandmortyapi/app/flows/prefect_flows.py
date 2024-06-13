from prefect import task, Flow
#from prefect.schedules import IntervalSchedule
from datetime import timedelta
import sys

sys.path.append('rickandmortyapi')

from app.services.data_extractor import DataExtractor


@task(retries=3, retry_delay_seconds=10)
def extract_characters():
    DataExtractor.extract_characters()


@task(retries=3, retry_delay_seconds=10)
def extract_episodes():
    DataExtractor.extract_episodes()


@task(retries=3, retry_delay_seconds=10)
def extract_locations():
    DataExtractor.extract_locations()


# schedule = IntervalSchedule(interval=timedelta(hours=1))


with Flow("RickAndMortyDataExtraction") as flow:
    #extract_characters()
    #extract_episodes()
    extract_locations()


if __name__ == "__main__":
    flow.run()
