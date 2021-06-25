from django.conf.urls import url
from pets import views

urlpatterns = [ 
    url(r'^api/pets$', views.pet_list),
    url(r'^api/pets/delete$', views.pet_list_delete),
    url(r'^api/pets/(?P<pk>[0-9]+)$', views.pet_detail)
]