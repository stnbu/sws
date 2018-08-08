from django.urls import path
from . import views

urlpatterns = [
    path('<str:current_tab>/', views.tab, name='tab'),
]
