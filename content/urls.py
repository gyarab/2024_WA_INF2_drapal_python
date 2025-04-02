from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('building/<int:id>', views.building),
    path('architect/<int:id>', views.architect),
    path('style/<int:id>', views.style),
]