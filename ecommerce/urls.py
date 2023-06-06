from django.urls import path
from .views import get_company,get_company_id,get_product


urlpatterns = [
    path('',get_company),
    path('<int:id>',get_company_id),
    path("<int:id>/products",get_product),
    path('<int:company_id>/produts/<int:id>',get_company_id)
]