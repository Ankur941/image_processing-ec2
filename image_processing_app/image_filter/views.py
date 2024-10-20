

from django.shortcuts import render #type: ignore
from django.core.files.storage import FileSystemStorage #type: ignore
from PIL import Image #type:ignore
import os

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)  # Save uploaded image
        uploaded_image_url = fs.url(filename)

        
        img = Image.open(fs.path(filename))
        processed_image_path = fs.path('processed_' + filename)
        img = img.convert('L')  # Convert image to grayscale as an example
        img.save(processed_image_path)
        processed_image_url = fs.url('processed_' + filename)

        return render(request, "image_filter/upload.html", {
            'uploaded_image_url': uploaded_image_url,
            'processed_image_url': processed_image_url
        })

    return render(request, "image_filter/upload.html")
