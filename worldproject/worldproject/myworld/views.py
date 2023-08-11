from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import world
from . forms import WorldForm
# Create your views here.

def index(request):
    obj = world.objects.all()
    return render(request, "home.html", {'result': obj})

def details(request,world_id):
    res=world.objects.get(id=world_id)
    return render(request, "detail.html", {'result': res})

def add_world(request):
    if request.method == "POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        obj=world(name=name,desc=desc,year=year,img=img)
        obj.save()

    return render(request,'add.html')

def update(request,id):
    space=world.objects.get(id=id)
    form = WorldForm(request.POST or None, request.FILES, instance=space)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'world': space})

def delete(request,id):
    if request.method =='POST':
        x=world.objects.get(id=id)
        x.delete()
        return redirect('/')
    return render(request,'delete.html')