from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from products.models import Product


class ProductList(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 6


class GuidesRecipesView(TemplateView):
    template_name = 'products/guides_recipes.html'


class CommunityView(TemplateView):
    template_name = 'products/community.html'


class ResourcesView(TemplateView):
    template_name = 'products/resources.html'


class ContactView(TemplateView):
    template_name = 'products/contact.html'


class ProductDetailsView(DetailView):
    template_name = 'products/product_details.html'
    queryset = (Product.objects.all()
                .select_related('category')
                .prefetch_related('reviews'))

    def get_context_data(self, **kwargs):
        product = Product.objects.get(slug=self.kwargs['slug'])
        context = super().get_context_data(**kwargs)
        context['product'] = product
        return context
