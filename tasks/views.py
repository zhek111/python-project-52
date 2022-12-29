from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites import requests
from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from statuses.forms import StatusCreateChangeForm
from statuses.models import Statuses
from django.utils.translation import gettext
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from tasks.forms import TaskCreateChangeForm, TaskFilterForm
from tasks.models import Tasks


class TasksView(LoginRequiredMixin, ListView):
    template_name = "tasks/index.html"
    model = Tasks
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = TaskFilterForm(self.request.GET)
        if form.is_valid():
            status = form.cleaned_data['status']
            executor = form.cleaned_data['executor']
            labels = form.cleaned_data['labels']
            only_my_tasks = form.cleaned_data['only_my_tasks']

            if status:
                queryset = queryset.filter(status=status)
            if executor:
                queryset = queryset.filter(executor=executor)
            if labels:
                queryset = queryset.filter(labels__in=labels).distinct()
            if only_my_tasks:
                queryset = queryset.filter(author=self.request.user)
            return queryset


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "tasks/create.html"
    form_class = TaskCreateChangeForm
    success_url = '/tasks'
    success_message = "Задача создана"
    model = Tasks
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    





class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = TaskCreateChangeForm
    template_name = 'tasks/update.html'
    success_url = '/tasks'
    model = Tasks
    success_message = 'Обновилось успешно'



class TaskDeleateView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'tasks/delete.html'
    success_url = '/tasks'
    model = Tasks
    success_message = 'Удалилось'

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.author != request.user:
            messages.error(request, "Вы не являетесь автором этой задачи")
            return redirect('list_tasks')
        return super().dispatch(request, *args, **kwargs)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Tasks
    template_name = 'tasks/detail.html'
    context_object_name = 'task'
    
def filter_tasks(request):
    tasks = Tasks.objects.all()
    form = TaskFilterForm(request.GET)
    if form.is_valid():
        status = form.cleaned_data['status']
        executor = form.cleaned_data['executor']
        labels = form.cleaned_data['labels']
        only_my_tasks = form.cleaned_data['only_my_tasks']
        if status:
            tasks = tasks.filter(status=status)
        if executor:
            tasks = tasks.filter(executor=executor)
        if labels:
            tasks = tasks.filter(labels__in=labels)
            if only_my_tasks:
                tasks = tasks.filter(author=request.user)
        return render(request, 'tasks/index.html',
                      {'tasks': tasks, 'form': form})

