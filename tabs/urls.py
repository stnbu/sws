from django.urls import path, include
from . import views

urlpatterns = [
    path(r'captcha/', include('captcha.urls')),
    path('<str:current_tab_name>/', views.tab, name='tab'),
]
