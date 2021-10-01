from core.models import Imagem, Analise
from core.serializers import AnaliseSerializer, ImagemSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView


class ImagemView(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer


class ImagemListView(ListAPIView):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']


class AnaliseView(viewsets.ModelViewSet):
    queryset = Analise.objects.all()
    serializer_class = AnaliseSerializer


class AnaliseListView(ListAPIView):
    queryset = Analise.objects.all()
    serializer_class = AnaliseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["nome"]
