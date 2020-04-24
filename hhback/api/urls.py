from django.urls import path
from api.views import VacancyView, VacancyDetailView,VacancyCompanyView
from api.views import CompanyView, CompanyDetailView

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('companies/', CompanyView.as_view()),
    path('companies/<int:pk>/', CompanyDetailView.as_view()),
    path('login/', obtain_jwt_token),
    # path('companies/', company_list),
    # path('companies/<int:company_id>/', company_detail),
    path('companies/vacancies/<int:pk>/', VacancyCompanyView.as_view()),
    path('vacancies/', VacancyView.as_view()),
    path('vacancies/<int:pk>/',VacancyDetailView.as_view() )
]
