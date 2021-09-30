from core.models import Imagem, Analise
from core.serializers import AnaliseSerializer, ImagemSerializer
from rest_framework import viewsets


class ImagemView(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer


class AnaliseView(viewsets.ModelViewSet):
    queryset = Analise.objects.all()
    serializer_class = AnaliseSerializer
