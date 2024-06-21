from .models import UserModel, ProductsModel
from rest_framework import serializers

class UserSerilazers(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model= ProductsModel
        fields = '__all__'