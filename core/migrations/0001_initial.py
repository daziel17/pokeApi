# Generated by Django 2.2.24 on 2021-09-23 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('pokemon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preevolution', to='core.Pokemon')),
            ],
        ),
    ]