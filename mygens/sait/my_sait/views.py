from django.shortcuts import render

# Create your views here.

def home(request):
    return(request, 'my_sait/templates/main/base.html')