from django.shortcuts import render,redirect
from . models import *

from .forms import MyForms

def home(request):
    if request.method == 'POST':
        form = MyForms(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            
            obj=MyForm()
            obj.Name=name
            obj.Age=age
            obj.save()
            return redirect('home')
        
    else:
        mydata=MyForm.objects.all()
        form = MyForms()
    return render(request, 'index.html', {'forms': mydata,'form': form})
        


