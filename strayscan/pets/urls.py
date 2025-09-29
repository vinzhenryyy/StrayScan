from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_pet, name='report_pet'),   
    path('lost/', views.get_lost_pets, name='lost_pets'),     
    path('found/', views.get_found_pets, name='found_pets'),    
    path('pet/<int:pk>/edit/', views.edit_pet, name='edit_pet'),   
    path('pet/<int:pk>/delete/', views.delete_pet, name='delete_pet'),  
    path('pet/<int:pk>/mark_found/', views.mark_as_found, name='mark_as_found'),
    path('<str:status>/delete_all/', views.delete_all_pets_by_status, name='delete_all_pets_by_status'),             
    path('login/', views.login, name='login_page'),
    path('', views.index, name='index_page'), 
    path('api/petlist/', views.PetList.as_view(), name='api_petlist'),
    path('api/lostpetlist/', views.LostPetList.as_view(), name='api_lostpetlist'),
    path('api/foundpetlist/', views.FoundPetList.as_view(), name='api_foundpetlist'),
]
