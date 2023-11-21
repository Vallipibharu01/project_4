from arjun.views import*
from django.urls import path
app_name='arjun'

urlpatterns=[
    path('pushpa/',pushpa,name='pushpa'),
    path('arya/',arya,name='arya'),
]