from rest_framework import serializers
from .models import ExtractedText

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedText
        fields = ['text']

