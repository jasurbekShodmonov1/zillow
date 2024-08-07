from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('signUp/', RegisterView.as_view(), name='signUp'),
]
