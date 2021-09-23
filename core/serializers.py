from rest_framework import serializers
from core.models import Pokemon


class PokemonEvolutionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class PokemonStatsSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    base_stat = serializers.IntegerField(read_only=True)


class PokemonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    height = serializers.IntegerField(read_only=True)
    weight = serializers.IntegerField(read_only=True)
    evolution = serializers.SerializerMethodField()

    stats = PokemonStatsSerializer(many=True, source='pokemonstats_set')

    def get_evolution(self, obj):
        pokemon_evolution = Pokemon.objects.filter(pokemon=obj)

        serializers_pre_evolution = None
        if obj.pokemon is not None:
            serializers_pre_evolution = PokemonEvolutionSerializer(obj.pokemon, many=False).data

        serializers_evolution = None
        if pokemon_evolution is not None:
            serializers_evolution = PokemonEvolutionSerializer(pokemon_evolution, many=True).data

        return {'pre_evolution': serializers_pre_evolution, 'evolution': serializers_evolution}


