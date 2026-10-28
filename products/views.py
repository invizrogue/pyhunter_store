from django.db.models import Q, QuerySet, Avg
from django.views.generic import ListView, TemplateView, DetailView

from products.models import Product
from loguru import logger

class ProductList(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 6
    ordering = ['-created_at']

    queryset = (Product.objects.all()
                .select_related('category')
                .prefetch_related('reviews')
                .annotate(rating=Avg('reviews__rating')))

    ORDERING_FIELDS = ['price', '-price', 'created_at', '-created_at',
                       'name', '-name', 'rating', '-rating']

    def get_queryset(self) -> QuerySet:
        q = super().get_queryset()
        cats = self.request.GET.get('categories')
        sorting = self.request.GET.get('sorting')
        search = self.request.GET.get('search')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        logger.debug(f'Get params: {self.request.GET}')
        if cats:
            cats = cats.split(',')
            q = q.filter(category__slug__in=cats)

        if search:
            q = q.filter(
                Q(name__icontains=search) | Q(description__icontains=search))

        if min_price and isinstance(min_price, (int, float)):
            # TODO: raise TypeError('Price must be a number')
            min_price = float(min_price)
            q = q.filter(price__gte=min_price)

        if max_price and isinstance(max_price, (int, float)):
            # TODO: raise TypeError('Price must be a number')
            max_price = float(max_price)
            q = q.filter(price__lte=max_price)

        if sorting and sorting in self.ORDERING_FIELDS:
            q = q.order_by(sorting)

        return q


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
