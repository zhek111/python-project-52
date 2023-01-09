from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext_lazy as _


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class LoginUserView(SuccessMessageMixin, LoginView):
    success_message = _('You are logged in')

    def form_invalid(self, form):
        messages.error(self.request, _('Please enter the correct username and password. Both fields can be case sensitive.'))
        return super().form_invalid(form)


class LogoutUserView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)


from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    a = None
    a.hello() # Creating an error with an invalid line of code
    return HttpResponse("Hello, world. You're at the pollapp index.")