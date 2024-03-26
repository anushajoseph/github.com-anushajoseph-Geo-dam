from django.shortcuts import render
from comparisonmodel import *
# Create your views here.
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser
# from .models import UploadedImages
# from .your_ml_file import predict  # Replace with your model's location

# class MultiImageUploadView(APIView):
#     parser_classes = [MultiPartParser]

#     def post(self, request, *args, **kwargs):
#         image1 = request.FILES['image1']
#         image2 = request.FILES['image2']

#         # Save uploaded images
#         uploaded_images = UploadedImages.objects.create(image1=image1, image2=image2)

#         # Load the model (assuming it's defined in your_ml_file.py)
#         model = load_model()  # Implement model loading logic (if separate)

#         # Preprocess images (adjust based on your model's requirements)
#         processed_image1 = preprocess_image(image1)
#         processed_image2 = preprocess_image(image2)

#         # Make prediction using the model
#         prediction = predict(processed_image1, processed_image2)

#         return Response({'prediction': prediction})

def output(request):
    if request.method == 'POST':
        image1= request.POST.get('image1')
        image2= request.POST.get('image2')
    
        