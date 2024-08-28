from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('services/', views.service_view, name='service_page')
]
