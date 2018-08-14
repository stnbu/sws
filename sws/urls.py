from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(url='/tabs/home/')),
    path('tabs/', include('tabs.urls')),
]

# completely disable admin UI in production
if settings.DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))
