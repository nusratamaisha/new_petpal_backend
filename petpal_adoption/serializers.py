from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    PetType, Breed, Pet, PetImage, Adopter, AdoptionApplication,
    Veterinarian, Product, ProductImage, ProductReview, Admin
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetType
        fields = ['id', 'name']


class BreedSerializer(serializers.ModelSerializer):
    pet_type = PetTypeSerializer(read_only=True)

    class Meta:
        model = Breed
        fields = ['id', 'name', 'pet_type']


class PetImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetImage
        fields = ['id', 'image_url']


class PetSerializer(serializers.ModelSerializer):
    type = PetTypeSerializer(read_only=True)
    breed = BreedSerializer(read_only=True)
    additional_images = PetImageSerializer(many=True, read_only=True)

    class Meta:
        model = Pet
        fields = '__all__'


class AdopterSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Adopter
        fields = ['id', 'user', 'phone', 'address']


class AdoptionApplicationSerializer(serializers.ModelSerializer):
    adopter = AdopterSerializer(read_only=True)
    pet = PetSerializer(read_only=True)

    class Meta:
        model = AdoptionApplication
        fields = ['id', 'adopter', 'pet', 'status', 'reason', 'created_at']


class VeterinarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinarian
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image_url']


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['id', 'name', 'rating', 'date', 'comment']


class ProductSerializer(serializers.ModelSerializer):
    additional_images = ProductImageSerializer(many=True, read_only=True)
    reviews = ProductReviewSerializer(many=True, read_only=True)
    pet_type = PetTypeSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Admin
        fields = ['id', 'user', 'role']
