from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from statuses.forms import StatusCreateChangeForm
from statuses.models import Status
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'next'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,
                           "You are not authorized! Please sign in.")
        return super().dispatch(request, *args, **kwargs)

class StatusView(CustomLoginRequiredMixin, ListView):
    template_name = "statuses/index.html"
    model = Status
    context_object_name = "statuses"


class StatusCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "statuses/create.html"
    form_class = StatusCreateChangeForm
    success_url = '/statuses'
    success_message = _("status created successfully")
    model = Status


class StatusUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = StatusCreateChangeForm
    template_name = 'statuses/update.html'
    success_url = '/statuses'
    model = Status
    success_message = _("status changed successfully")
    

class StatusDeleateView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'statuses/delete.html'
    success_url = '/statuses'
    model = Status
    success_message = _("status successfully deleted")
    def dispatch(self, request, *args, **kwargs):
        status = self.get_object()
        if status.tasks.exists():
            messages.error(request,
                           _("Can't delete status because it's in use"))
            return redirect('list_statuses')
        return super().dispatch(request, *args, **kwargs)