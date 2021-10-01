import pytest
from core.models import Imagem, Analise
from datetime import datetime
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


# Estou tendo com problema com pytest, por isso repetir
# a função aqui no testes
def create_image():
    image = BytesIO()
    Image.new('RGB', (100, 100)).save(image, 'JPEG')
    image.seek(0)
    image_memory = SimpleUploadedFile('image.jpg', image.getvalue())
    return image_memory


imagem_memory = create_image()


@pytest.mark.django_db
def test_get_file_name():
    Imagem.objects.create(
        nome="teste",
        imagem=imagem_memory
    )
    assert Imagem.objects.get(nome="teste").nome == "teste"


@pytest.mark.django_db
def test_has_one_image():
    Imagem.objects.create(
        nome="teste",
        imagem=imagem_memory
    )
    assert Imagem.objects.count() == 1


@pytest.mark.django_db
def test_get_analise_name():
    imagem = Imagem.objects.create(
        nome="teste",
        imagem=imagem_memory
    )

    Analise.objects.create(
        nome="teste",
        imagem=imagem,
        tipo="teste",
        status="A"
    )
    assert Analise.objects.get(nome="teste").nome == "teste"


@pytest.mark.django_db
def test_has_one_analise():
    imagem = Imagem.objects.create(
        nome="teste",
        imagem=""
    )
    Analise.objects.create(
        nome="teste",
        imagem=imagem,
        tipo="teste",
        criado_em=datetime.now(),
        atualizado_em=datetime.now(),
        status="A"
    )
    assert Imagem.objects.count() == 1
