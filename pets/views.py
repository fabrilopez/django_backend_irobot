from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .models import Pet
from .serializers import PetSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


@api_view(['GET','POST'])
def pet_list(request):
    # GET a full list of pets, POST create a new pet
    if request.method == 'GET':
        pets = Pet.objects.all()

        user = request.user
        print('user_id: ', user.id)
        
        # read search criteria
        name = request.GET.get('name', None)
        age = request.GET.get('age', None)

        # filters by name
        if name is not None and age is None:
            pets = pets.filter(name__icontains=name)

        # filters by age
        elif age is not None and name is None:
        	# just in case a STRING appears, who knows..
        	try:
        		pets = pets.filter(age=age)
        	except ValueError:
        		return JsonResponse({'message': 'Field (age) expected a number but got ({})'.format(age)}, status=status.HTTP_404_NOT_FOUND) 
        
        # serialize response
        pets_serializer = PetSerializer(pets, many=True)
        return JsonResponse(pets_serializer.data, safe=False)

    elif request.method == 'POST':
        pet_data = JSONParser().parse(request)
        pet_serializer = PetSerializer(data=pet_data)

        # if "valid", persist
        if pet_serializer.is_valid():
            pet_serializer.save()
            return JsonResponse(pet_serializer.data, status=status.HTTP_201_CREATED) 
        # return error
        return JsonResponse(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['DELETE',])
def pet_list_delete(request):
    # DELETE erase all pets
    if request.method == 'DELETE':

        count = Pet.objects.all().delete()
        return JsonResponse({'message': '{} All Pets records were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE',])
def pet_detail(request, pk):
    # GET pet detail, PUT modifies pet details, DELETE erase pet record
    
    # first checks if find pet by pk (id)
    try: 
        pet = Pet.objects.get(pk=pk) 
    except Pet.DoesNotExist: 
        return JsonResponse({'message': 'The pet record does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # done, now GET, PUT and DELETE by pk
 
    if request.method == 'GET': 
        pet_serializer = PetSerializer(pet) 
        return JsonResponse(pet_serializer.data)

    elif request.method == 'PUT': 
        pet_data = JSONParser().parse(request) 
        pet_serializer = PetSerializer(pet, data=pet_data) 
        if pet_serializer.is_valid(): 
            pet_serializer.save() 
            return JsonResponse(pet_serializer.data) 
        return JsonResponse(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        pet.delete() 
        return JsonResponse({'message': 'Pet record was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)