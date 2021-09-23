from django.urls import path
from . import views

find_pokemon = views.PokemonViewSet.as_view({
    'get': 'findByName'
})

urlpatterns = [
    path('pokemon/<str:name>/', find_pokemon, name='find_pokemon')
]
