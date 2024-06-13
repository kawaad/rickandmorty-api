from prefect import task, flow
import django

django.setup()


@task(name="CharacterExtraction", retries=3, retry_delay_seconds=10)
def extract_characters_task(data_extractor):
    data_extractor.extract_characters()


@task(name="EpisodeExtraction", retries=3, retry_delay_seconds=10)
def extract_episodes_task(data_extractor):
    data_extractor.extract_episodes()


@task(name="LocationExtraction", retries=3, retry_delay_seconds=10)
def extract_locations_task(data_extractor):
    data_extractor.extract_locations()


@flow(name="RickAndMortyDataExtraction")
def extract_flow():
    extract_characters_task()
    extract_episodes_task()
    extract_locations_task()


if __name__ == "__main__":
    extract_flow()
