from django.contrib import admin
from .models import Info, PostDetails, Testimonial, PaymentDetails, Products

# Register your models here.
# @admin.register(Info)
admin.site.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']
    
# admin.site.register(Membership)
# admin.site.register(UserMembership)
# admin.site.register(Subscription)
admin.site.register(PostDetails)
admin.site.register(Testimonial)
admin.site.register(PaymentDetails)
admin.site.register(Products)


