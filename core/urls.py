
from django.urls import path
from django.urls.conf import include
from core import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('imagens', views.ImagemView)
router.register('analises', views.AnaliseView)

urlpatterns = [
    path("api/v1/", include(router.urls))
]
