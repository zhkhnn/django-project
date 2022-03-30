from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .forms import NameForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from .forms import *
from .models import *

def index(request):
    return render(request, 'myapp/yoga.html')

# def home(request):
#   # if this is a POST request we need to process the form data
#   if request.method == 'POST':
#     # create a form instance and populate it with data from the request:
#     form = NameForm(request.POST)
#     # check whether it's valid:
#     if form.is_valid():
#         p = Info()
#         p.name = form.cleaned_data['name']
#         p.email = form.cleaned_data['email']
#         p.subject = form.cleaned_data['subject']
#         p.message = form.cleaned_data['message']
#         p.save()
#         # redirect to a new URL:
#         return HttpResponseRedirect('')
#   else:
#     form = NameForm()
#
#   return render(request, 'myapp/yoga.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Info.objects.create(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'myapp/yoga.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'myapp/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

    def get_user_context(self, **kwargs):

        context = kwargs
        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'myapp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    # def get_success_url(self):
    #     return reverse_lazy('/')


    def get_user_context(self, **kwargs):
        context = kwargs
        return context


def logout_user(request):
    logout(request)
    return redirect('login')


# def autho(request):
#   if request.method == 'POST':
#     form = LoginUserForm(request.POST)
#     if form.is_valid():
#       post = form.save(commit=False)
#       post.user = request.user
#       post.save()
#       return redirect('index')
#   else:
#       posts = Info.objects.filter(hidden=False).all()
#
#   context = {'form': form, 'posts': posts}
#
#   return render(request, 'myapp/yoga.html', context)
