from django.urls import path
from .views import *

urlpatterns = [        
    path('train_model', train_model, name='train_model'),
    path('predict', predict, name='predict'),
]