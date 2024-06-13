from django.urls import path

from .views import (CharacterAPIView, CharacterListAPIView,
                    EpisodeListAPIView, EpisodeAPIView,
                    LocationListAPIView, LocationAPIView)

urlpatterns = [
    path('episodes/', EpisodeListAPIView.as_view(), name='episodes-list'),
    path('episode/<int:source_id>/', EpisodeAPIView.as_view(), name='episodes-detail'),
    path('locations/', LocationListAPIView.as_view(), name='locations-list'),
    path('location/<int:source_id>/', LocationAPIView.as_view(), name='locations-detail'),
    path('characters/', CharacterListAPIView.as_view(), name='characters-list'),
    path('character/<int:source_id>/', CharacterAPIView.as_view(), name='characters-detail'),

]
