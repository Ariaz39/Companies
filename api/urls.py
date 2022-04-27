from django.urls import path

from api.views import CompanyView, OfficesView

urlpatterns = [
    path('companies/', CompanyView.as_view(), name='companies_list'),
    path('companies/<int:id>', CompanyView.as_view(), name='companies_process'),
    path('offices/', OfficesView.as_view(), name='offices_list'),
    path('offices/<int:id>', OfficesView.as_view(), name='offices_process'),
]
