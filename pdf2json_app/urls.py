from django.urls import path
from . import views

urlpatterns = [
    path("pdf-to-json/", views.pdf_to_json, name="pdf_to_json"),
    path("", views.home),
]
