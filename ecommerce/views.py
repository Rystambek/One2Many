from django.http import HttpRequest,JsonResponse
from .models import Company,Product
import json

def to_company(company:Company) -> dict:
    return {
        'id' : company.pk,
        'name': company.name,
        'website':company.website
    }

def to_product(product:Product) -> dict:
    return {
        'id':product.pk,
        'company_id' : product.company.pk,
        'name' : product.name,
        'price' : product.price
    }

def get_company(request:HttpRequest) -> JsonResponse:
    if request.method == 'GET':
        companies = Company.objects.all()
        result = [to_company(company) for company in companies]

        return JsonResponse(result,safe=False)