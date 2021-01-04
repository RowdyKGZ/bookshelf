from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from account.forms import UserRegistrationForm


class RegisterView(FormView):
    """Create user"""
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'account/registration.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_valid(form)
