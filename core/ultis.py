from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


def create_image():
    image = BytesIO()
    Image.new('RGB', (100, 100)).save(image, 'JPEG')
    image.seek(0)
    image_memory = SimpleUploadedFile('image.jpg', image.getvalue())
    return image_memory
