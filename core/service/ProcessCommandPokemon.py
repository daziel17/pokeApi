import requests
from core.models import Pokemon, PokemonStats


class ProcessCommandPokemon:
    def __init__(self):
        self.pokemons = []
        self.pokemons_stats = []

    def execute(self, id_evolution_chain: int):
    
        evolution_chain = self.call_service("https://pokeapi.co/api/v2/evolution-chain/" + str(id_evolution_chain))

        if evolution_chain is not None:
            if evolution_chain['chain'] is not None:

                if len(evolution_chain['chain']['evolves_to']):
                    self.get_evolution(evolution_chain['chain'], None)

        for pokemon in self.pokemons:

            if not Pokemon.objects.filter(pk=pokemon.id).exists():
                pokemon.save()

                for stat in filter(lambda a: a.pokemon.id == pokemon.id, self.pokemons_stats):
                    pokemon.pokemonstats_set.add(stat, bulk=False)

        return self.pokemons

    def get_evolution(self, evolution, parent):

        #consultar especie de la evolución
        species = self.call_service(evolution['species']['url'])

        if species is not None:
            # iterar las variedes pokemon
            for variety_pokemon in species['varieties']:

                pokemon = self.call_service(variety_pokemon['pokemon']['url'])

                if pokemon is not None:

                    new_pokemon = Pokemon()
                    new_pokemon.id = pokemon['id']
                    new_pokemon.name = pokemon['name']
                    new_pokemon.height = pokemon['height']
                    new_pokemon.weight = pokemon['weight']
                    new_pokemon.pokemon = parent

                    if pokemon['stats'] is not None:
                        for stat in pokemon['stats']:

                            new_stat = PokemonStats()
                            new_stat.pokemon = new_pokemon
                            new_stat.name = stat['stat']['name']
                            new_stat.base_stat = stat['base_stat']
                            self.pokemons_stats.append(new_stat)

                    self.pokemons.append(new_pokemon)

                    if evolution is not None and len(evolution['evolves_to']) > 0:
                        self.get_evolution(evolution['evolves_to'][0], new_pokemon)

    def call_service(self, url: str):
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            return response.json()
        return None


