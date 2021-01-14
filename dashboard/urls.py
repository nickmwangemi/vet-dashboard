from django.urls import path, include
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('vets', views.vet_records, name='all'),
    path('vets/new', views.onboard_vet, name='new'),
    path('vets/<int:pk>', views.vet_record_detail, name='record_detail'),

]
