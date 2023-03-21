from django.urls import path
from gaurdians.views import *

app_name='gaurdians'

urlpatterns=[
    path('Groot/',Groot,name='Groot'),
]