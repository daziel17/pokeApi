from django.core.management.base import BaseCommand
from core.service.ProcessCommandPokemon import ProcessCommandPokemon


class Command(BaseCommand):
    help = 'Input to ID of evolution chain'

    def add_arguments(self, parser):
        parser.add_argument('ID', nargs=1, type=int)

    def handle(self, *args, **options):

        id = options.get("ID", None)

        if(id is not None):

            process = ProcessCommandPokemon()
            process.execute(id[0])
            self.stdout.write("Proceso ejecutado con éxito!")
        else:
            self.stdout.write("Debe especificar un id para realizar el proceso")




