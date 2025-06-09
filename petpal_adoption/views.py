from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *

# --- Pet Related Views ---

class PetTypeViewSet(viewsets.ModelViewSet):
    queryset = PetType.objects.all()
    serializer_class = PetTypeSerializer
    permission_classes = [permissions.AllowAny]


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [permissions.AllowAny]


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.AllowAny]


class PetImageViewSet(viewsets.ModelViewSet):
    queryset = PetImage.objects.all()
    serializer_class = PetImageSerializer
    permission_classes = [permissions.AllowAny]

# --- Adopter and Adoption Application Views ---

class AdopterViewSet(viewsets.ModelViewSet):
    queryset = Adopter.objects.all()
    serializer_class = AdopterSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdoptionApplicationViewSet(viewsets.ModelViewSet):
    queryset = AdoptionApplication.objects.all()
    serializer_class = AdoptionApplicationSerializer
    #permission_classes = [permissions.IsAuthenticated]

# --- Veterinarian Views ---

class VeterinarianViewSet(viewsets.ModelViewSet):
    queryset = Veterinarian.objects.all()
    serializer_class = VeterinarianSerializer
    permission_classes = [permissions.AllowAny]

# --- Product Views ---

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.AllowAny]


class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [permissions.AllowAny]

# --- Admin View ---

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAdminUser]

# --- API Overview Route ---

@api_view(['GET'])
def api_list(request):
    api_urls = {
        'Pets': '/pets/',
        'Pet Types': '/pet-types/',
        'Breeds': '/breeds/',
        'Pet Images': '/pet-images/',
        'Adopters': '/adopters/',
        'Adoption Applications': '/adoption-applications/',
        'Veterinarians': '/veterinarians/',
        'Products': '/products/',
        'Product Images': '/product-images/',
        'Product Reviews': '/product-reviews/',
        'Admins': '/admins/',
    }
    return Response(api_urls)
