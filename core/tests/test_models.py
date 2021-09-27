from django.test import TestCase
from core.models import Image, Analise
from django.core.files import File
from datetime import datetime


class ImageTest(TestCase):
    """Test module for image"""

    def setUp(self) -> None:
        Image.objects.create(
            name="teste", 
            image=File(file=b"")
        )
    
    def test_get_file_name(self):
        result = Image.objects.get(name="teste")
        expect = "teste"
        self.assertEqual(result.name, expect)

        
    def test_has_one_image(self):
        result = Image.objects.count()
        self.assertEqual(result, 1)


class AnaliseTest(TestCase):
    """Test module for analise"""

    def setUp(self) -> None:
        image = Image.objects.create(
            name="teste", 
            image=File(file=b"")
        )
        Analise.objects.create(
            name="teste",
            image=image,
            type="teste",
            created_at=datetime.now(),
            status="A"
        )
    def test_get_analise_name(self):
        result = Analise.objects.get(name="teste")
        expect = "teste"
        self.assertEqual(result.name, expect)

    
    def test_has_one_analise(self):
        result = Analise.objects.count()
        self.assertEqual(result, 1)