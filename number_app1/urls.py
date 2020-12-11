from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('inspect', views.inspect),
    path('toohigh', views.toohigh),
    path('toolow', views.toolow),
    path('exactly', views.exactly),
]