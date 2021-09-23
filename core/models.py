from django.db import models


# Create your models here.
class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    height = models.IntegerField()
    weight = models.IntegerField()
    pokemon = models.ForeignKey('self', null=True, blank=True, related_name="preevolution", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' pre_evolution: ' + (self.pokemon.name if self.pokemon is not None else 'None')


class PokemonStats(models.Model):

    pokemon = models.ForeignKey(Pokemon, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    base_stat = models.IntegerField()
