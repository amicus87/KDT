from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import hospital

def index(request):
    dashboard_hospital = hospital.objects.all()
    context = {'dashboard_hospital': dashboard_hospital}
    return render(request, 'hospital/index.html', context)

def index1(request):
    return render(request, 'barchart1.html')
