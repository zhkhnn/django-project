from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.forms import ModelForm


class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class PostDetails(models.Model):
    name = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name



class PaymentDetails(models.Model):
    card_number = models.IntegerField()
    month_year = models.IntegerField()
    cvv = models.IntegerField()
    name = models.CharField(max_length=25)
    zip = models.IntegerField()
    state = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PaymentForm(ModelForm):
    class Meta:
        model = PaymentDetails
        fields = '__all__'


class Products(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    what_you_need = models.CharField(max_length=80)
    flow_speed = models.CharField(max_length=100)
    sweat_factor = models.CharField(max_length=40)
    zen_factor = models.CharField(max_length=80)
    def __str__(self):
        return self.name






# MEMBERSHIP_CHOICES = (('Beginner', 'beginner'), ('Intermediate', 'inter'), ('Advanced', 'advanced'), ('Professional', 'pro'))
# class Membership(models.Model):
#     slug = models.SlugField()
#     membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default='beginner', max_length=30)
#     price = models.IntegerField()
#     stripe_plan_id = models.CharField(max_length=40)
#     def __str__(self):
#         return self.membership_type
#
#
#
# class UserMembership(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     stripe_customer_id = models.CharField(max_length=40)
#     membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
#
#     def __str__(self):
#         return self.user.username
#
#
# class Subscription(models.Model):
#     user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
#     stripe_subscription_id = models.CharField(max_length=40)
#     active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.user_membership.user.username
#
# def post_save_user_membership_create(sender, instance, created, *args, **kwargs):
#     if created:
#         UserMembership.objects.get_or_create(user=instance)
#
#     user_membership, created = UserMembership.objects.get_or_create(user=instance)
#
#     if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id == '':
#         new_customer_id = stripe.Customer.create(email=instance.email)
#         user_membership.stripe_customer_id = new_customer_id['id']
#         user_membership.save()
#
#
# post_save.connect(post_save_user_membership_create, sender=settings.AUTH_USER_MODEL)
