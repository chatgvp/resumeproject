from django.shortcuts import render


import PyPDF2
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from transformers import AutoTokenizer, LlamaForCausalLM

model = LlamaForCausalLM.from_pretrained("gpena8826/resumeproject")
tokenizer = AutoTokenizer.from_pretrained("gpena8826/resumeproject")

prompt = "Hey, are you conscious? Can you talk to me?"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate
generate_ids = model.generate(
    inputs.input_ids, attention_mask=inputs.attention_mask, max_length=30
)
generated_text = tokenizer.decode(generate_ids[0], skip_special_tokens=True)

print(generated_text)


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
