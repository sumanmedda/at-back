from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserModel, ProductsModel
from .serializers import UserSerilazers, ProductsSerializers
from rest_framework.response import Response
# Create your views here.

class ProductsViews(APIView):
    def get(self, request):
        products = ProductsModel.objects.all()
        serializer = ProductsSerializers(products, many=True)
        return Response({"status":200,"message": "Products Fetched", "items":serializer.data},)
    
    def post(self, request):
        data = request.data
        serializer = ProductsSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":201, "message": "Product Added", "items":serializer.data},)
        else:
            return Response({"status":400, "message": "Something went wrong", "items":serializer.errors},)
    
