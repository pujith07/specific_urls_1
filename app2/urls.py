from django.urls import path
from app2.views import *

app_name='nothing'

urlpatterns=[
    path('kholi/',kholi,name='kholi'),
    path('abd/',abd,name='abd'),
]