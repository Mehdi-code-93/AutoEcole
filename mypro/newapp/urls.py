from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('addrec/', views.addrec, name='addrec'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('update/uprec/<int:id>/', views.uprec, name='uprec'),
    path('creneaux/<int:id>/', views.creneaux, name='creneaux'),
    path('addcreneau/', views.add_creneau, name='addcreneau'),  # Route supplémentaire pour ajouter des créneaux
]
