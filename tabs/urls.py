from django.urls import path
from . import views

urlpatterns = [
    path('<str:label>/', views.tab, name='tab'),
]
