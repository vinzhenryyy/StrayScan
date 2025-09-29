from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, mixins
from .serializers import PetSerializer
import json, re

from .models import PetLog

class SecurePetList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pets = PetLog.objects.all().values()
        return JsonResponse({'pets': list(pets)})
    
def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
@permission_classes([AllowAny])
def report_pet(request):
    data = json.loads(request.body)
    contact = data.get('contact_info', '').strip()
    pet_type = data.get('pet_type', '').strip().lower()

    phone_pattern = r'^\d{11}$'
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

    pet_types = {
        'antelope', 'badger', 'bat', 'bear', 
        'bee', 'beetle', 'bison', 'boar', 'bird',
        'butterfly', 'cat', 'chimpanzee', 'cow', 
        'coyote', 'crab', 'crow', 'deer', 
        'dog', 'dolphin', 'donkey', 'dragonfly', 
        'duck', 'eagle', 'elephant', 'flamingo', 
        'fox', 'goat', 'goldfish', 'goose', 'gorilla', 
        'hamster', 'hare', 'hedgehog', 'hippopotamus', 
        'hornbill', 'horse', 'hummingbird', 'hyena', 
        'jellyfish', 'kangaroo', 'koala', 'ladybugs', 
        'leopard', 'lion', 'lizard', 'lobster',
        'moth', 'mouse', 'octopus', 'okapi', 'orangutan', 
        'otter', 'owl', 'ox', 'oyster', 'panda', 'pelecaniformes', 
        'penguin', 'pig', 'pigeon', 'porcupine', 'possum', 'raccoon', 
        'rat', 'reindeer', 'rhinoceros', 'sandpiper', 'seahorse', 
        'seal', 'shark', 'sheep', 'snake', 'sparrow', 'squid', 
        'squirrel', 'starfish', 'swan', 'tiger', 'turkey', 
        'turtle', 'whale', 'wolf', 'wombat', 'woodpecker', 'zebra', 
        'others'
    }

    if not re.match(phone_pattern, contact) and not re.match(email_pattern, contact):
        return JsonResponse({'error': 'Contact info must be a valid 11-digit number or a valid email address.'}, status=400)
    if pet_type not in pet_types:
        return JsonResponse({'error': 'Invalid pet type. Allowed types: Dog, Cat, Bird, Hamster, Others, Etc...'}, status=400)
    try:
        pet = PetLog.objects.create(
            pet_name=data.get('pet_name'),
            pet_type=data['pet_type'],
            description=data['description'],
            status=data['status'],
            location=data['location'],
            date=parse_date(data['date']),
            contact_info=contact
        )
        return JsonResponse({'message': 'Pet reported successfully', 'id': pet.id}, status=201)
    except KeyError as e:
        return JsonResponse({'error': f'Missing field: {e}'}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_lost_pets(request):
    lost_pets = list(PetLog.objects.filter(status='lost').values())
    return JsonResponse({'lost_pets': lost_pets})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_found_pets(request):
    found_pets = list(PetLog.objects.filter(status='found').values())
    return JsonResponse({'found_pets': found_pets})

@api_view(['PUT'])
@permission_classes([AllowAny])
def edit_pet(request, pk):
    pet = get_object_or_404(PetLog, id=pk)
    data = json.loads(request.body)
    for field in ['pet_name', 'pet_type', 'description', 'status', 'location', 'contact_info']:
        if field in data:
            setattr(pet, field, data[field])
    if 'date' in data:
        pet.date = parse_date(data['date'])
    pet.save()
    return JsonResponse({'message': 'Pet log updated successfully'})

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_pet(request, pk):
    pet = get_object_or_404(PetLog, id=pk)
    pet.delete()
    return JsonResponse({'message': 'Pet log deleted'})

@api_view(['POST'])
@permission_classes([AllowAny])
def mark_as_found(request, pk):
    if request.method == 'POST':
        try:
            pet = PetLog.objects.get(pk=pk, status='lost')
            pet.status = 'found'
            pet.save()
            return JsonResponse({'message': 'Pet marked as found successfully.'})
        except PetLog.DoesNotExist:
            return JsonResponse({'error': 'Lost pet not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_all_pets_by_status(request, status):
    if status not in ['lost', 'found']:
        return JsonResponse({'error': 'Invalid status'}, status=400)
    PetLog.objects.filter(status=status).delete()
    return JsonResponse({'message': f'All {status} pet logs deleted'})

@permission_classes([AllowAny])
class PetList(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PetLog.objects.all()
    serializer_class = PetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

@permission_classes([AllowAny])
class LostPetList(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PetLog.objects.filter(status='lost').values()
    serializer_class = PetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

@permission_classes([AllowAny])
class FoundPetList(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PetLog.objects.filter(status='found').values()
    serializer_class = PetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    