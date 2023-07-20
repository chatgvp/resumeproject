import PyPDF2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PDFSerializer
from django.shortcuts import render
import pdfplumber
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json


@api_view(["POST"])
def pdf_to_json(request):
    if "pdf_file" in request.FILES:
        pdf_file = request.FILES["pdf_file"]
        # with open(pdf_file, "rb") as f:
        #     pdf = PyPDF2.PdfReader(f)
        #     text = ""
        #     for page in pdf.pages:
        #         text += page.extract_text()
        #     print(text)
        sample_json_data = {"key": "value"}
        json_data = json.dumps(sample_json_data, cls=DjangoJSONEncoder)

        return JsonResponse(json_data, safe=False)

    return JsonResponse({"error": "No PDF file provided."}, status=400)


def home(request):
    return render(request, "home.html")
