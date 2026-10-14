from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from products.models import Product


class ProductList(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class GuidesRecipesView(TemplateView):
    template_name = 'products/guides-recipes.html'


class CommunityView(TemplateView):
    template_name = 'products/community.html'


class ResourcesView(TemplateView):
    template_name = 'products/resources.html'


class ContactView(TemplateView):
    template_name = 'products/contact.html'
