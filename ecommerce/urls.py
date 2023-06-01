from django.urls import path
from .views import get_company


urlpatterns = [
    path('',get_company)
]