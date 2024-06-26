from django.db import models

# Create your models here.


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    dimension = models.CharField(max_length=100)
    source_id = models.IntegerField(unique=True)
    residents = models.ManyToManyField('Character', related_name='residents_locations')
    url = models.URLField(unique=True, null=True, blank=True)
    created = models.DateTimeField()

    class Meta:
        verbose_name = "Location"

    def __str__(self):
        return self.name


class Episode(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    air_date = models.CharField(max_length=100)
    episode = models.CharField(max_length=100)
    source_id = models.IntegerField(unique=True)
    characters = models.ManyToManyField('Character', related_name='episode_characters')
    url = models.URLField(unique=True, null=True, blank=True)
    created = models.DateTimeField()

    class Meta:
        verbose_name = "Episode"

    def __str__(self):
        return self.name


class Character(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    type = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100)
    source_id = models.IntegerField(unique=True)
    origin = models.ForeignKey('Location', on_delete=models.SET_NULL,
                               null=True, related_name='origin_characters')
    location = models.ForeignKey('Location', on_delete=models.SET_NULL,
                                 null=True, related_name='current_characters')
    image = models.URLField(null=True, blank=True)
    url = models.URLField(unique=True, null=True, blank=True)
    created = models.DateTimeField()

    class Meta:
        verbose_name = "Character"

    def __str__(self):
        return self.name

    def get_episodes(self):
        return self.episode_characters.all()

    def set_episodes(self, episodes):
        self.episode_characters.set(episodes)
