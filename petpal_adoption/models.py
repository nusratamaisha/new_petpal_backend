from django.db import models
from django.contrib.auth.models import User

class PetType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=100)
    pet_type = models.ForeignKey(PetType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.pet_type.name})"

class Pet(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(PetType, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
    size = models.CharField(max_length=10, choices=[("Small", "Small"), ("Medium", "Medium"), ("Large", "Large")])
    color = models.CharField(max_length=50)
    vaccinated = models.BooleanField(default=False)
    neutered = models.BooleanField(default=False)
    good_with_kids = models.BooleanField(default=False)
    description = models.TextField()
    personality = models.TextField()
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    image = models.URLField()
    
    def __str__(self):
        return self.name


class PetImage(models.Model):
    pet = models.ForeignKey(Pet, related_name="additional_images", on_delete=models.CASCADE)
    image_url = models.URLField()

    
class Adopter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class AdoptionApplication(models.Model):
    #adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True)
    #status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    name = models.TextField(blank=True, null=True, default="")
    email = models.EmailField(blank=True, null=True, default="")
    address = models.TextField(blank=True, null=True, default="")
    experience = models.TextField(blank=True, null=True, default="")
    homeType = models.TextField(blank=True, null=True, default="")
    reason = models.TextField(blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.pet}"


class Veterinarian(models.Model):
    name = models.CharField(max_length=100)
    clinic = models.CharField(max_length=100)
    specialties = models.JSONField()
    rating = models.FloatField()
    review_count = models.PositiveIntegerField()
    address = models.CharField(max_length=200,blank=True, null=True)
    location = models.CharField(max_length=100,blank=True, null=True)
    phone = models.CharField(max_length=20)
    hours = models.CharField(max_length=100)
    image = models.URLField()
    description = models.TextField()
    next_available = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    pet_type = models.ForeignKey(PetType, on_delete=models.SET_NULL, null=True)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    weight = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    image = models.URLField()
    in_stock = models.BooleanField(default=True)
    rating = models.FloatField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="additional_images", on_delete=models.CASCADE)
    image_url = models.URLField()


class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField()
    date = models.DateField()
    comment = models.TextField()



class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default="Admin")

    def __str__(self):
        return self.user.username

