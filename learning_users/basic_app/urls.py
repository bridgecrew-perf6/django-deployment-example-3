from django.conf.urls import url
from basic_app import views
from django.urls import path

#TEMPLATE URLs

app_name = 'basic_app'

urlpatterns=[
    path('register/',views.register, name='register')
]
