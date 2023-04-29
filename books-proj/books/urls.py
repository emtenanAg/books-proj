from django.urls import path
from . import views

urlpatterns = [
    path('', views.Recommendation, name='Recommendation'),
    path('result', views.Result, name='Result')
]
