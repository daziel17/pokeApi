# Generated by Django 2.2.24 on 2021-09-24 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pokemonstats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='pokemon',
        ),
        migrations.AlterModelTable(
            name='pokemonstats',
            table='core_pokemon_stats',
        ),
        migrations.CreateModel(
            name='PokemonEvolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evolution_pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_evolution', to='core.Pokemon')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_base', to='core.Pokemon')),
            ],
            options={
                'db_table': 'core_pokemon_evolutions',
            },
        ),
    ]
