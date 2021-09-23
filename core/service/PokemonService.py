from core.models import Pokemon
from core.serializers import PokemonSerializer


class PokemonService:
    def findByName(self, pokemon_name: str):

        try:
            pokemon = Pokemon.objects.get(name__iexact=pokemon_name)
            return PokemonSerializer(pokemon).data
        except Pokemon.DoesNotExist:
            return {"status": "error", "message": "Pokemon not found"}
