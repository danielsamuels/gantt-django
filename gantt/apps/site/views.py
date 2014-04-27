from django.views.generic import TemplateView, CreateView, FormView
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse

from .forms import UserCreationForm
from .models import Organisation


class Application(TemplateView):
    template_name = "application.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(Application, self).dispatch(request, *args, **kwargs)
        else:
            return redirect_to_login(request.path)


class Registration(CreateView):
    form_class = UserCreationForm
    template_name = "auth/registration.html"

    def form_valid(self, form):
        self.object = form.save()

        user = authenticate(
            username=form.cleaned_data.get('email_address'),
            password=form.cleaned_data.get('password')
        )

        login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('site:application')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('site:application'))
        else:
            return super(Registration, self).dispatch(request, *args, **kwargs)


class Login(FormView):
    form_class = AuthenticationForm
    template_name = "auth/login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('site:application'))
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
