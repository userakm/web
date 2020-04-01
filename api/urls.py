from django.urls import path
from api.views import company_list, company_detail, company_vacancy, vacancy_detail, vacancy_list, vacancies_top_ten
urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_detail),
    path('companies/<int:company_id>/vacancies/', company_vacancy),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('vacancies/top_ten/', vacancies_top_ten),
]