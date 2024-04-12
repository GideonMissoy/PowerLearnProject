from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/task_list.html'

class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'base/task_form.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')