import pytest
from core.models import Image, Analise
from datetime import datetime


@pytest.mark.django_db
def test_get_file_name():
    Image.objects.create(
        name="teste",
        image=""
    )
    assert Image.objects.get(name="teste").name == "teste"


@pytest.mark.django_db
def test_has_one_image():
    Image.objects.create(
        name="teste",
        image=""
    )
    assert Image.objects.count() == 1


@pytest.mark.django_db
def test_get_analise_name():
    image = Image.objects.create(
        name="teste",
        image=""
    )

    Analise.objects.create(
        name="teste",
        image=image,
        type="teste",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        status="A"
    )
    assert Analise.objects.get(name="teste").name == "teste"


@pytest.mark.django_db
def test_has_one_analise():
    image = Image.objects.create(
        name="teste",
        image=""
    )
    Analise.objects.create(
        name="teste",
        image=image,
        type="teste",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        status="A"
    )
    assert Image.objects.count() == 1
