from django.urls import path
from . import views

urlpatterns = [
    path('<str:current_tab_name>/', views.tab, name='tab'),
]
