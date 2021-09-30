from rest_framework import serializers
from core.models import Imagem, Analise


class AnaliseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analise
        fields = "__all__"
        read_only_fields = ("created_at",)


class ImagemSerializer(serializers.ModelSerializer):
    analises = AnaliseSerializer(many=True, read_only=True)

    class Meta:
        model = Imagem
        fields = ["nome", "imagem", "analises"]
