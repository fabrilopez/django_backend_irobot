from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns


from accounts import views


urlpatterns = [
    path('profile/', views.ProfileView.as_view()),
    path('api/auth/', views.CustomAuthToken.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)