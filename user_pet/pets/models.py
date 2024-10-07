from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    CATEGORY_CHOICES = [
        ('cat', 'Кот'),
        ('dog', 'Собака'),
        ('rodent', 'Грызун'),
        ('fish', 'Рыбки'),
        ('other', 'Другое'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    pet_category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    pet_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.pet_name}"
