from django.urls import path
from .views import pet_form_view, create_pet

urlpatterns = [
    path('pet-form/', pet_form_view, name='pet_form'),
    path('api/pet/', create_pet, name='create_pet'),
]
