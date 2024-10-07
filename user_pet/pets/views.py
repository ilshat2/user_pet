from django.shortcuts import render
from .forms import PetForm
from django.contrib.auth.decorators import login_required 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PetSerializer
from rest_framework import status

@login_required  
def pet_form_view(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False) 
            pet.user = request.user 
            pet.save() 
            return render(request, 'pets/success.html', {'name': pet.name, 'pet_name': pet.pet_name})
    else:
        form = PetForm()
    return render(request, 'pets/pet_form.html', {'form': form})

@api_view(['POST'])
def create_pet(request):
    if request.method == 'POST':
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
