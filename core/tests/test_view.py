import json
from datetime import datetime

import pytest
from core.models import Analise, Imagem
from core.serializers import AnaliseSerializer
from rest_framework import status
from core.ultis import create_image


# initialize the APIClient app
@pytest.fixture
def create_models():
    imagem_memory = create_image()

    imagem = Imagem.objects.create(
        nome="teste1",
        imagem=imagem_memory
    )
    image2 = Imagem.objects.create(
        nome="teste2",
        imagem=imagem_memory
    )
    Analise.objects.create(
        nome="teste",
        imagem=imagem,
        tipo="teste",
        status="A"
    )
    Analise.objects.create(
        nome="teste2",
        imagem=image2,
        tipo="teste2",
        status="A"
    )


@pytest.mark.django_db
def test_view_get_all_images(client, create_models):
    url = "http://127.0.0.1:8000/api/v1/imagens/"
    response = client.get(url)
    images = Imagem.objects.count()
    assert response
    assert images == len(response.data)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_view_search_imagem_by_name(client, create_models):
    url = "http://127.0.0.1:8000/api/v1/imagens/?search=teste1/"
    response = client.get(url)
    assert response
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_view_get_single_image(client, create_models):
    url = "http://127.0.0.1:8000/api/v1/imagens/1/"
    response = client.get(url)
    assert response
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_view_get_wrong_image(client):
    url = "http://127.0.0.1:8000/api/v1/imagens/30/"
    response = client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_create_new_image(client):
    image_memory = create_image()

    valid_payload = {
        "nome": "teste3",
        "imagem": image_memory
    }
    url = "http://127.0.0.1:8000/api/v1/imagens/"
    response = client.post(
      url, data=valid_payload
    )
    imagem = Imagem.objects.last()
    assert imagem.nome == "teste3"
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_try_create_invalid_image(client):
    invalid_payload = {
            "nome": 10.0,
            "imagem": 10.0,
        }
    url = "http://127.0.0.1:8000/api/v1/imagens/"
    response = client.post(url, data=invalid_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_try_update_wrong_image(client, create_models):
    invalid_payload = {
            "teste": "teste",
            "teste": "teste"
        }
    url = "http://127.0.0.1:8000/api/v1/imagens/30/"
    response = client.put(url, data=invalid_payload)
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_delete_image(client, create_models):
    url = "http://127.0.0.1:8000/api/v1/imagens/1/"
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_delete_wrong_image(client, create_models):
    url = "http://127.0.0.1:8000/api/v1/imagens/30/"
    response = client.delete(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND


# tests for analises
@pytest.mark.django_db
def test_view_get_all_analises(client, create_models):
    url = "http://127.0.0.1:8000/api/v1/analises/"
    response = client.get(url)
    analises = Analise.objects.all()
    serializer = AnaliseSerializer(analises, many=True)

    assert response.data == serializer.data
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_view_search_anlise_by_name(client, create_models):
    url = "http://127.0.0.1:8000/api/v1/analises/?search=teste2/"
    response = client.get(url)
    assert response
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_view_get_single_analise(client, create_models):
    analise = Analise.objects.get(pk=1)
    url = "http://127.0.0.1:8000/api/v1/analises/1/"
    response = client.get(url)
    serializer = AnaliseSerializer(analise)
    assert response.data == serializer.data
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_view_get_wrong_analise(client):
    url = "http://127.0.0.1:8000/api/v1/analises/10/"
    response = client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_create_new_analise(client, create_models):

    imagem = Imagem.objects.get(pk=2)
    date = datetime.now()
    date = date.strftime("%Y-%m-%d")
    valid_payload = {
            "nome": "teste1",
            "imagem": imagem.pk,
            "tipo": "teste",
            "status": "A"

        }

    url = "http://127.0.0.1:8000/api/v1/analises/"

    response = client.post(
        path=url,
        data=json.dumps(valid_payload),
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_try_create_invalid_analise(client, create_models):
    invalid_payload = {
            "nome": "",
            "imagem": "",
            "tipo": "",
            "status": ""
        }
    url = "http://127.0.0.1:8000/api/v1/analises/"
    response = client.post(
        url,
        data=json.dumps(invalid_payload),
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_delete_analise(client, create_models):
    url = "http://127.0.0.1:8000/api/v1/analises/1/"
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_delete_wrong_analise(client, create_models):
    url = "http://127.0.0.1:8000/api/v1/analises/10/"
    response = client.delete(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
