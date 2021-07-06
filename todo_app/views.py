from django.shortcuts import render,redirect

from .forms import todoforms
from .models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class TaskListView(ListView):
    model = task
    template_name = 'task_view.html'
    context_object_name = 'obj1'

class TaskDetailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'j'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})

class TaskDelete(DeleteView):
    model = task
    template_name = 'delete.html'
    context_object_name = 'c'
    reverse_lazy('index')

def task_view(request):
    obj1=task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date = request.POST.get('date')
        t=task(name=name, priority=priority,date=date)
        t.save()
    return render(request,'task_view.html',{'obj1':obj1})

def delete(request,taskid):
    obj2=task.objects.get(id=taskid)
    if request.method=='POST':
        obj2.delete()
        return redirect('/')
    return render(request,'delete.html',{'obj2':obj2})

def update(request,id):
    obj3=task.objects.get(id=id)
    form=todoforms(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'obj3':obj3,'form':form})




