from django.views import View
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')


class LoginUserView(LoginView):
    pass

class LogoutUserView(LogoutView):
    pass
    