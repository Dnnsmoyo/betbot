from django.shortcuts import render

# Create your views here.
from .models import Employee, Car
from .serializers import EmployeeSerializer, CarSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse_lazy
import numpy as np
from sklearn.linear_model import LinearRegression

def index(request):
  
    return render(request,'myapi/landing2.html')
