from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def newsignup(request):
    return render(request,'index.html', {"form":UserCreationForm})
# Create your views here.
