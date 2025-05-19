from django.shortcuts import render
from .forms import EnForms
from .models import EnModel

def home(request):
    if request.method=="POST":
        na=request.POST.get("name")
        em=request.POST.get("email")
        ph=request.POST.get("phone")
        data=EnModel(name=na,email=em,phone=ph)
        data.save()
        fm=EnForms()
        return render(request,"home.html",{"fm":fm,"msg":"Record added"})
    else:
        fm=EnForms()
        return render(request,"home.html",{"fm":fm,})
# Create your views here.
