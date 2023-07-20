from django.shortcuts import render


import PyPDF2
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


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


# class PdfToJsonView(APIView):
#     def post(self, request, *args, **kwargs):
#         if "pdf_file" in request.FILES:
#             pdf_file = request.FILES["pdf_file"]
#             file_path = default_storage.save(
#                 pdf_file.name, ContentFile(pdf_file.read())
#             )
#             response_data = {
#                 "file_name": pdf_file.name,
#                 "file_path": file_path,
#                 "file_size": pdf_file.size,
#             }
#             return Response(response_data)
#         else:
#             return Response({"error": "No PDF file was uploaded."}, status=400)


def home(request):
    return render(request, "home.html")
