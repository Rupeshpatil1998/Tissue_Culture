from django.shortcuts import render,redirect,get_object_or_404
from Tissue.models import database#connecting database with views
from Tissue.forms import databaseForm#connecting user form
from Tissue.forms import ContactForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    contactform=ContactForm(request.POST or None)
    if contactform.is_valid():
        contactform.save()
        return redirect('home')
    return render(request,'contact.html',{'form':contactform})
@login_required


def rupesh11add(request):
    rupesh11form=databaseForm(request.POST or None)
    if rupesh11form.is_valid():
        rupesh11form.save()
        return redirect("rupesh11list")
    return render(request,'rupesh11add.html',{'form':rupesh11form})

@login_required


def rupesh11list(request):
    allfeedback=database.objects.all()
    return render(request,'rupesh11list.html',{'rupesh11s':allfeedback})
@login_required


def rupesh11edit(request,pk):
    rupesh11=get_object_or_404(database,pk=pk)
    rupesh11form=databaseForm(request.POST or None,instance=rupesh11)
    if rupesh11form.is_valid():
        rupesh11form.save()
        return redirect("rupesh11list")
    return render(request,'rupesh11add.html',{'form':rupesh11form})
@login_required

def rupesh11delete(request,pk):
    rupesh11=get_object_or_404(database,pk=pk)
    if request.method=='POST':
        rupesh11.delete()
        return redirect('rupesh11list')
    return render(request,'rupesh11delete.html',{'rupesh11':rupesh11})

def banana(request):
    return render(request,'banana.html')


def flower(request):
    return render(request,'flower.html')

