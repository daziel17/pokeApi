from rest_framework import serializers


class PokemonStatsSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    base_stat = serializers.IntegerField(read_only=True)


class PokemonEvolutionPartialSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, source="evolution_pokemon.id")
    name = serializers.CharField(read_only=True, source="evolution_pokemon.name")


class PokemonPreEvolutionPartialSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, source="pokemon.id")
    name = serializers.CharField(read_only=True, source="pokemon.name")


class EvolutionSerializer(serializers.Serializer):
    pre_evolution = PokemonPreEvolutionPartialSerializer(source='pokemon_evolution', many=True)
    evolution = PokemonEvolutionPartialSerializer(source='pokemon_base', many=True)


class PokemonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    height = serializers.IntegerField(read_only=True)
    weight = serializers.IntegerField(read_only=True)
    evolutions = serializers.SerializerMethodField()
    stats = PokemonStatsSerializer(many=True, source='pokemonstats_set')

    def get_evolutions(self, obj):

        return EvolutionSerializer(obj, many=False).data



