from django.template.defaulttags import url
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact,  name='contact'),
     path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]