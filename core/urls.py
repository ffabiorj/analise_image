
from django.urls import path
from core import views

urlpatterns = [
    path("api/v1/images", views.get_delete_update_image, name="get_delete_update_image"),
    path("api/v1/images", views.get_post_image, name="get_post_images"),
    path("api/v1/analises", views.get_delete_update_analise, name="get_delete_update_analise"),
    path("api/v1/analises", views.get_post_analise, name="get_post_analise")
]
