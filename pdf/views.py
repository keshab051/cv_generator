from django.shortcuts import render
from .models import profile

def accept(request):
    return render(request,'pdf/accept.html')

# Create your views here.
