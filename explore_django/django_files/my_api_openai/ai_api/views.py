from django.shortcuts import render

# Create your views here.
# aiapi/views.py
from django.http import JsonResponse
import openai

def generate_text(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            openai.api_key = settings.OPENAI_API_KEY
            response = openai.Completion.create(
                engine="text-davinci-001",
                prompt=text,
                # Additional parameters
            )
            generated_text = response.choices[0].text
            return JsonResponse({"generated_text": generated_text})
        else:
            return JsonResponse({"error": "Text is required."}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)
