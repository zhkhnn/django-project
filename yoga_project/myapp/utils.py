from .models import *

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        info = Info.objects.all()

