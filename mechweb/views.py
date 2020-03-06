from django.shortcuts import render
from .models import MechHomePage
# Create your views here.

# from wagtail.contrib.modeladmin.options import ModelAdmin
# from .models import Person

# class PersonAdmin(ModelAdmin):
#     model = Person
#     list_display = ('first_name', 'last_name')
	
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    return HttpResponseRedirect(reverse('social:begin', args=['azuread-tenant-oauth2']))