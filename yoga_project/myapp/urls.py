from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact,  name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('like/<int:pk>/', AddLike.as_view(), name='like'),
    path('dislike/<int:pk>/', Dislike.as_view(), name='dislike'),
    path('base/', base, name='base'),
    path('price', products, name='price'),
    path('faq', TemplateView.as_view(template_name='myapp/faq.html'), name='faq'),
    path('testimonial', TemplateView.as_view(template_name='myapp/testimonial.html'), name='testimonial'),
    path('upload', image_upload_view, name='upload'),
    path('payment', TemplateView.as_view(template_name='myapp/payment.html'), name='payment'),
    path('success', payment, name='success'),
    path('products', products, name='products'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)