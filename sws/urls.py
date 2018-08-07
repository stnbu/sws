from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tabs/', include('tabs.urls')),
    path('admin/', admin.site.urls),
]
