from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from statuses.views import CustomLoginRequiredMixin
from tasks.forms import TaskCreateChangeForm, TaskFilterForm
from tasks.models import Task
from django.utils.translation import gettext_lazy as _


class TasksView(CustomLoginRequiredMixin, ListView):
    template_name = "tasks/index.html"
    model = Task
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


class TaskCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "tasks/create.html"
    form_class = TaskCreateChangeForm
    success_url = '/tasks'
    success_message = _("Task created successfully")
    model = Task

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = TaskCreateChangeForm
    template_name = 'tasks/update.html'
    success_url = '/tasks'
    model = Task
    success_message = _('Task changed successfully')


class TaskDeleateView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'tasks/delete.html'
    success_url = '/tasks'
    model = Task
    success_message = _('Task deleted successfully')

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.author != request.user:
            messages.error(request,
                           _('A task can only be deleted by its author.'))
            return redirect('list_tasks')
        return super().dispatch(request, *args, **kwargs)


class TaskDetailView(CustomLoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    context_object_name = 'task'


def filter_tasks(request):
    tasks = Task.objects.all()
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
