import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Company, Offices


# Create your views here.
class OfficesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            offices = list(Offices.objects.filter(id=id).values())
            if len(offices) > 0:
                office = offices[0]
                data = {'message': 'Oficina detallada correctamente'}
            else:
                data = {'message': 'No existe la oficina indicada'}
            return JsonResponse(data)
        else:
            offices = list(Offices.objects.values())
            if len(offices) > 0:
                data = {'message': 'Oficinas listadas con exito', 'Oficinas': offices}
            else:
                data = {'message': 'No existen oficinas.'}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Offices.objects.create(name=jd['name'], city=jd['city'])

        data = {'message': 'Oficina creada con exito'}
        return JsonResponse(data)

    def put(self, request, id=id):
        jd = json.loads(request.body)
        office = Offices.objects.get(id=id)
        office.name = jd['name']
        office.city = jd['city']
        office.save()
        data = {'message': 'Oficina actualizada con exito'}
        return JsonResponse(data)

    def delete(self, request, id=id):
        offices = Offices.objects.filter(id=id).values()
        if len(offices) > 0:
            office = Offices.objects.get(id=id)
            office.delete()
            data = {'message': 'Oficina eliminada con exito'}
        else:
            data = {'message': 'No existe la oficina indicada'}
        return JsonResponse(data)


class CompanyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos = {'message': 'Compania listadas correctamente.', 'company': company}
            else:
                datos = {'companies': 'Compania not found...'}
            return JsonResponse(datos)
        else:
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos = {'message': 'Companies listadas correctamente.', 'companies': companies}
            else:
                datos = {'message': 'Companies not found...'}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Company.objects.create(
            name=jd['name'],
            website=jd['website'],
            foundation=jd['foundation'],
            office_id = jd['office_id']
        )
        datos = {'message': 'Compania agregada correctamente'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        print(jd)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.office_id = jd['office_id']
            company.save()

            datos = {'message': 'Company actualizada con exito'}
        else:
            datos = {'message': 'Company not found...'}
        return JsonResponse(datos)

    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company.objects.get(id=id).delete()

            datos = {'message': 'Company eliminada con exito'}
        else:
            datos = {'message': 'Company not found...'}
        return JsonResponse(datos)
