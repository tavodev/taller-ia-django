
from django.http import JsonResponse
from django.shortcuts import render
from website.form import ImageForm
from website.utils import process_image, get_openai_response
import time
def index(request):
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            base64_image = process_image(image)
            result = get_openai_response(base64_image)
            return JsonResponse({'result': result})
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, 'website/index.html', context)
