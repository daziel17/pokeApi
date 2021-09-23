from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from core.service.PokemonService import PokemonService


# Create your views here.
class PokemonViewSet(viewsets.GenericViewSet):

    @action( detail=False, methods=['get'])
    def findByName(self, request, name):
        service = PokemonService()
        return Response(service.findByName(name))


