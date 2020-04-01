from django.shortcuts import render

from django.http.response import JsonResponse

from api.models import Company
from api.models import Vacancy


def company_list(request):
    c_list = Company.objects.all()
    companies_json = [company.to_json() for company in c_list]
    return JsonResponse(companies_json, safe=False)


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(company.to_json(), safe=False)


def company_vacancy(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    vacancies = company.vacancy_set.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_list(request):
    v_list = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in v_list]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(vacancy.to_json(), safe=False)


def vacancies_top_ten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)