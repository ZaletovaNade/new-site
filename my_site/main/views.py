# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Table
from .forms import TableForm

def home(request):
    table=Table.objects.all()
    return render(request, "main/home.html", {'table':table})
def text(request):
    if request.method=="POST":
        form=TableForm(request.POST)
        form.save()
    
    
    form=TableForm()
    context = {'form': form}
    
    return render(request, "main/text.html", context)

