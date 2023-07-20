from django.shortcuts import render


import PyPDF2
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Use a pipeline as a high-level helper
# from transformers import pipeline

# pipe = pipeline("text-generation", model="meta-llama/Llama-2-70b-chat-hf")


class PdfToJsonView(APIView):
    def post(self, request, *args, **kwargs):
        if "pdf_file" in request.FILES:
            pdf_file = request.FILES["pdf_file"]
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            response_data = text
            return Response(response_data, content_type="application/json")
        else:
            return Response({"error": "No PDF file was uploaded."}, status=400)


def home(request):
    return render(request, "home.html")
