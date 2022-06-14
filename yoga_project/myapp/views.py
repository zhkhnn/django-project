import stripe
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.views import View

from .forms import NameForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from .forms import *
from .models import *

def index(request):
    post = PostDetails.objects.all()
    context = {
        'posts': post,
    }
    return render(request, 'myapp/yoga.html', context)

def base(request):
    return render(request, 'myapp/base.html')

def products(request):
    post = Products.objects.all()
    context = {
        'material': post,
    }
    return render(request, 'myapp/pricing.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Info.objects.create(name=name, email=email, subject=subject, message=message)
        contact.listed_by = request.user
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

class AddLike(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        post = PostDetails.objects.get(pk=pk)
        all_post = PostDetails.objects.all()
        context = {
            'posts': all_post,
        }

        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislike.remove(request.user)

        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if not is_like:
            post.likes.add(request.user)
        if is_like:
            post.likes.remove(request.user)
        return render(request, 'myapp/yoga.html', context)


class Dislike(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        post = PostDetails.objects.get(pk=pk)
        all_post = PostDetails.objects.all()
        context = {
            'posts': all_post,
        }

        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        if not is_dislike:
            post.dislikes.add(request.user)
        if is_dislike:
            post.dislikes.remove(request.user)
        return render(request, 'myapp/yoga.html', context)

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'myapp/testimonial.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'myapp/testimonial.html', {'form': form})



def payment(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # form = PaymentForm(request.POST)
        # # check whether it's valid:
        # if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            card_number = request.POST.get('card_number', False)
            month_year = request.POST.get('month_year', False)
            cvv = request.POST.get('cvv', False)
            name = request.POST.get('name', False)
            zip = request.POST.get('zip', False)
            state = request.POST.get('state', False)
            contact = PaymentDetails.objects.create(card_number=card_number,
                                             month_year=month_year, cvv=cvv,
                                             name=name, zip=zip, state=state)
            # contact.listed_by = request.user
            contact.save()
            return redirect('/')

        # if a GET (or any other method) we'll create a blank form
    else:
        # form = PaymentForm()
        return render(request, 'myapp/base.html')







# def get_user_membership(request):
#     user_membership_qs = UserMembership.objects.filter(user=request.user)
#     if user_membership_qs.exists():
#         return user_membership_qs.first()
#     return None
#
# def get_user_subscription(request):
#     user_subscription_qs = Subscription.objects.filter(user_membership=get_user_membership(request))
#     if user_subscription_qs.exists():
#         user_subscription = user_subscription_qs.first()
#         return user_subscription
#     return None
#
# def get_selected_membership(request):
#     membership_type = request.session['selected_membership_type']
#     selected_membership_qs = Membership.objects.filter(membership_type=membership_type)
#     if selected_membership_qs.exists():
#         return selected_membership_qs.first()
#     return None
#
#
# class MembershipSelectView(ListView):
#     model = Membership
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         current_membership = get_user_membership(self.request)
#         context['current_membership'] = str(current_membership.membership)
#         return context
#
#     def post(self, request, **kwargs):
#         selected_membership = request.POST.get('membership_type')
#         user_subscription = get_user_subscription(request)
#         user_membership = get_user_membership(request)
#
#         selected_membership_qs = Membership.objects.filter(membership_type=selected_membership)
#         if selected_membership_qs.exists():
#             selected_membership = selected_membership_qs.first()
#
#
#         if user_membership.membership == selected_membership:
#             if user_subscription != None:
#                 messages.info(request, "You have already this membership")
#                 return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#
#         request.session['selected_membership_type'] = selected_membership.membership_type
#
#         return HttpResponseRedirect(reverse(''))
#
#
# # def PaymentView(request):
# #     user_membership = get_user_membership(request)
# #     selected_membership = get_selected_membership(request)
#
#
# def cancel_subscription(request):
#     user_sub = get_user_subscription(request)
#
#     if user_sub.active == False:
#         messages.info(request, 'You don`t have an active membership')
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#
#     sub = stripe.Subscription.retrieve(user_sub.stripe_subscription_id)
#     sub.delete()
#     user_sub.active = False
#     user_sub.save()
#
#     free_membership = Membership.objects.filter(membership_type='Beginner').first()
#     user_membership = get_user_membership(request)
#     user_membership.membership = free_membership
#     user_membership.save()
#
#     messages.info(request, 'You successfully canceled membership')
#
#     return redirect('/member/')
#
