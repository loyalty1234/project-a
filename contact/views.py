from django.shortcuts import render
from . import views

# Create your views here.
def contact_view(request):
    return render(request, 'contact_form.html')