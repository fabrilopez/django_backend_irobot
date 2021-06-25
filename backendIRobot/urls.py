from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include 

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    url(r'^', include('pets.urls'))
]
