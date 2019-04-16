from django.views.generic.edit import CreateView, FormView, View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.shortcuts import redirect

from account.forms import RegistrationForm, LoginForm


class AccountRegistrationFormView(CreateView):
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        account = form.instance
        account.set_password(form.cleaned_data['password'])

        return super().form_valid(form)


class AccountLoginFormView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('dishes_list')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        account = authenticate(self.request,
                               username=username, password=password)

        if account:
            login(self.request, account)
            return super().form_valid(form)
        else:
            return redirect(reverse_lazy('login'))


class AccountLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)

        return redirect(reverse_lazy('login'))