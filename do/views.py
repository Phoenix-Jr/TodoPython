from django.shortcuts import render,redirect,get_object_or_404
from .forms import FormTask
from .models import Task

# Create your views here.


def index(request):
    form = FormTask(request.POST or None)
    if form.is_valid():
        form.save()
    all_task = Task.objects.all()
    context = {
        'form':form,
        'taches':all_task
    }
    return render(request,'index.html',context)

def update(request,myid):
    object = get_object_or_404(Task,id=myid)
    form = FormTask(request.POST or None,instance=object)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form})

def delete(request,myid):
    object = get_object_or_404(Task,id=myid)
    object.delete()
    return redirect('/')