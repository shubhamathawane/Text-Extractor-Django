from django.urls import path
from .views import extracted_text_view

urlpatterns = [
    path('extracted_text/', extracted_text_view, name='extract_text'),
]