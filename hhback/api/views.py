from django.http import JsonResponse
from django.shortcuts import render
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, CompanyDetailSerializer
from api.serializers import VacancySerializer, VacancyDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class CompanyView(APIView):
    def get(self, request, format=None):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailView(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanyDetailSerializer(company)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanyDetailSerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VacancyView(APIView):
    def get(self, request, format=None):
        vacancy = Vacancy.objects.all()
        serializer = VacancySerializer(vacancy, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class VacancyCompanyView(APIView):
     def get(self, request, pk, format=None):
        vacancy = Vacancy.objects.filter(company=pk)
        serializer = VacancySerializer(vacancy, many=True)
        return Response(serializer.data)

        
class VacancyDetailView(APIView):
    def get_object(self, pk):
        try:
            return Vacancy.objects.get(id=pk)
        except Vacancy.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vacancy = self.get_object(pk)
        serializer = VacancyDetailSerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        vacancy = self.get_object(pk)
        serializer = VacancyDetailSerializer(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vacancy = self.get_object(pk)
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# def company_list(request):
#     companies = Company.objects.all()
#     companies_json = [company.to_json() for company in companies]
#     return JsonResponse(companies_json, safe=False)

# def company_detail(request, company_id):
#     try:
#         company = Company.objects.get(id=company_id)
#     except Company.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#     return JsonResponse(company.to_json())

# def company_vacancies(request, company_id):
#     try:
#         vacancies = Vacancy.objects.filter(company__id=company_id)
#         vacancies_json = [vacancy.to_json() for vacancy in vacancies]
#     except Vacancy.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#     return JsonResponse(vacancies_json, safe=False)

# def vacancy_list(request):
#     vacancies = Vacancy.objects.all();
#     vacancies_json = [vacancy.to_json() for vacancy in vacancies]
# #   return JsonResponse(vacancies_json, safe=False)

#def vacancy_detail(request, vacancy_id):
    #try:
      #  vacancy = Vacancy.objects.get(id=vacancy_id)
   # except Vacancy.DoesNotExist as e:
       # return JsonResponse({'error': str(e)})
   # return JsonResponse(vacancy.to_json())

#def vacancy_top_ten(request):
   # vacancies = Vacancy.objects.all().order_by('-salary')[:10]
   # vacancies_json = [vacancy.to_json() for vacancy in vacancies]
   # return JsonResponse(vacancies_json, safe=False)

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        # 'user': UserSerializer(user, context={'request': request}).data
    }