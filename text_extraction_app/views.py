from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.files.base import ContentFile
from .models import ExtractedText
from .serializers import TextSerializer
from PIL import Image
import pytesseract
import csv
import io
from .forms import ImageUploadForm


def extracted_text_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image_file']

            image = Image.open(uploaded_image)

            extracted_text = pytesseract.image_to_string(image)

            handwritten_text = recognize_handwriting(image)

            key_value_pairs = [line.split(':', 1) for line in extracted_text.split('\n') if ':' in line]
            extracted_data = {}
            for key, value in key_value_pairs:
                extracted_data[key.strip()] = value.strip()

            # Save extracted text to the database
            ExtractedText.objects.create(text=extracted_text)

            return render(request, 'text_extractor/extracted_text.html', {'extracted_text': extracted_data, 'handwritten_text': handwritten_text})
    else:
        form = ImageUploadForm()

    return render(request, 'text_extractor/upload_form.html', {'form': form})



def recognize_handwriting(image):
    return pytesseract.image_to_string(image, config='--oem 1 --psm 6')

