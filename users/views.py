from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import SignUpForm, ProfileForm

# Sign Up View
from .models import User, UserProfile


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    success_url = reverse_lazy('home')
    form_class = ProfileForm
    template_name = 'profile.html'

    def get_form_kwargs(self):
        kwargs = super(ProfileView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        first_name = form.data['first_name']
        last_name = form.data['last_name']
        username = form.data['username']
        email = form.data['email']
        user = self.request.user
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print("invalid")
        print(form)
        return super().form_invalid(form)
