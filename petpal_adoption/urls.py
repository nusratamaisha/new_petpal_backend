from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'pet-types', PetTypeViewSet, basename='pet-types')
router.register(r'breeds', BreedViewSet, basename='breeds')
router.register(r'pets', PetViewSet, basename='pets')
router.register(r'pet-images', PetImageViewSet, basename='pet-images')
router.register(r'adopters', AdopterViewSet, basename='adopters')
router.register(r'adoption-applications', AdoptionApplicationViewSet, basename='adoption-applications')
router.register(r'veterinarians', VeterinarianViewSet, basename='veterinarians')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'product-images', ProductImageViewSet, basename='product-images')
router.register(r'product-reviews', ProductReviewViewSet, basename='product-reviews')
router.register(r'admins', AdminViewSet, basename='admins')

urlpatterns = [
    path('', include(router.urls)), 
    path('api-list/', api_list, name='api-list'),
]
