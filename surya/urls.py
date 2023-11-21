from surya.views import *
from django.urls import path
app_name='surya'

urlpatterns=[
    path('gajini/',gajini,name='gajini'),
    path('brothers/',brothers,name='brothers'),
]