from django.urls import path,include
from . import views
urlpatterns = [
   
    path('about/', views.about),
    path('context/', views.context),
    path('services/', views.services),
    
]
