from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_papers, name='search_papers'),
    path('saved/', views.saved_papers, name='saved_papers'),
    path('save_paper/', views.save_paper, name='save_paper'),
    path('remove_paper/', views.remove_paper, name='remove_paper'),
]
