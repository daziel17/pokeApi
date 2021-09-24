import requests
from django.db import transaction
from core.models import Pokemon, PokemonStats, PokemonEvolution


class ProcessCommandPokemon:
    def __init__(self):
        self.pokemons = []
        self.pokemons_stats = []
        self.pokemons_evolutions = []

    def execute(self, id_evolution_chain: int):

        print("Inicio consulta api evolution chain")
        evolution_chain = self.call_service("https://pokeapi.co/api/v2/evolution-chain/" + str(id_evolution_chain))

        if evolution_chain is not None:
            if evolution_chain['chain'] is not None:

                if len(evolution_chain['chain']['evolves_to']):
                    print("Obtener evoluciones")
                    self.get_evolution(evolution_chain['chain'], None)

        print("Insertar pokemon's")
        with transaction.atomic():

            for pokemon in self.pokemons:
                if not Pokemon.objects.filter(pk=pokemon.id).exists():
                    pokemon.save()
                    for stat in filter(lambda a: a.pokemon.id == pokemon.id, self.pokemons_stats):
                        pokemon.pokemonstats_set.add(stat, bulk=False)
                    PokemonEvolution.objects.bulk_create(list(filter(lambda a: a.pokemon.id == pokemon.id,
                                                                     self.pokemons_evolutions)))

        return self.pokemons

    def get_evolution(self, evolution, parent):

        #consultar especie de la evolución
        species = self.call_service(evolution['species']['url'])

        if species is not None:
            # iterar las variedes pokemon
            for variety_pokemon in species['varieties']:

                pokemon = self.call_service(variety_pokemon['pokemon']['url'])

                exists_pokemon = list(filter(lambda a: a.id == pokemon['id'], self.pokemons))

                if pokemon is not None and  not len(exists_pokemon):

                    new_pokemon = Pokemon()
                    new_pokemon.id = pokemon['id']
                    new_pokemon.name = pokemon['name']
                    new_pokemon.height = pokemon['height']
                    new_pokemon.weight = pokemon['weight']

                    if pokemon['stats'] is not None:
                        for stat in pokemon['stats']:

                            new_stat = PokemonStats()
                            new_stat.pokemon = new_pokemon
                            new_stat.name = stat['stat']['name']
                            new_stat.base_stat = stat['base_stat']
                            self.pokemons_stats.append(new_stat)

                    self.pokemons.append(new_pokemon)
                    if parent is not None:
                        self.pokemons_evolutions.append(PokemonEvolution(pokemon=parent,
                                                                         evolution_pokemon=new_pokemon))

                else:
                    if parent is not None:
                        self.pokemons_evolutions.append(PokemonEvolution(pokemon=parent,
                                                                         evolution_pokemon=exists_pokemon[0]))

                if evolution is not None and len(evolution['evolves_to']) > 0:
                    self.get_evolution(evolution['evolves_to'][0], new_pokemon)

    def call_service(self, url: str):
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            return response.json()
        return None


