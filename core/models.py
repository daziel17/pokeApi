from django.db import models


# Create your models here.
class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    height = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return str(self.id) + ' ' + self.name


class PokemonStats(models.Model):

    pokemon = models.ForeignKey(Pokemon, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    base_stat = models.IntegerField()

    class Meta:
        '''
        se asigna el nombre de la tabla en la base de datos
        '''
        db_table = "core_pokemon_stats"


class PokemonEvolution(models.Model):

    pokemon = models.ForeignKey(Pokemon, null=False, blank=False, related_name='pokemon_base', on_delete=models.CASCADE)
    evolution_pokemon = models.ForeignKey(Pokemon, null=False, blank=False, related_name='pokemon_evolution', on_delete=models.CASCADE)

    def __str__(self):
        return 'Pokemon base: ' + (self.pokemon.name if self.pokemon is not None else 'None') + \
               ' Pokemon Evolution: ' + (self.evolution_pokemon.name if self.evolution_pokemon is not None else 'None')

    class Meta:
        '''
        se asigna el nombre de la tabla en la base de datos
        '''
        db_table = "core_pokemon_evolutions"