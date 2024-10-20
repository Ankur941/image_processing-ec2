# image_filter/urls.py

from django.urls import path #type: ignore
from . import views

urlpatterns = [
    path('', views.upload_image, name='http://127.0.0.1:8000/'),  # Image upload page
]
