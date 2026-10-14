from django.urls import path

from products.apps import ProductsConfig
from products.views import ProductList, GuidesRecipesView, CommunityView, \
    ResourcesView, ContactView

app_name = ProductsConfig.name

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('guides-recipes/', GuidesRecipesView.as_view(), name='guides_recipes'),
    path('community/', CommunityView.as_view(), name='community'),
    path('resources/', ResourcesView.as_view(), name='resources'),
    path('contact/', ContactView.as_view(), name='contact'),
]
