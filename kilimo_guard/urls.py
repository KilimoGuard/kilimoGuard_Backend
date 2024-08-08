from django.urls import path
from .views import *

urlpatterns = [        
    path('train_model', train_model, name='train_model'),
    path('predict', predict, name='predict'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]