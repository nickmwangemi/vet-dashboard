from django.urls import path, include
from . import views


urlpatterns = [
    # API Endpoints
    path('vets', views.VeterinaryOfficerList.as_view()),
    path('vets/new', views.VeterinaryOfficerList.as_view()),
    path('vets/<int:pk>', views.VeterinaryOfficerDetail.as_view()),

]
