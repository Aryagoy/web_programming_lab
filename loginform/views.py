from django.shortcuts import render
from .models import loginform
from .forms import login_form

def my_view(request):
    form=login_form(request.POST or None)
    if form.is_valid():
        form.save()
        form=login_form()
    context={
    
        'form':form
    }    
   
    return render(request,"loginform/index.html",context)