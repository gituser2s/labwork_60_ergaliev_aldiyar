from django.urls import path
from webapp.views.products import ProductDetail, ProductUpdateView, ProductCreateView, ProductDeleteView, ProductConfirmDeleteView
from webapp.views.base import IndexView
from webapp.views.baskets import ProductInBasketView, BasketView, DeleteProductInBasketView, ConfirmDeleteProductInBasketView


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/confirm_delete/', ProductDeleteView.as_view(), name='product_confirm_delete'),
    path('basket/add', ProductInBasketView.as_view(), name='basket_add'),
    path('basket/', BasketView.as_view(), name='basket_index'),
    path('basket/<int:pk>/delete/', DeleteProductInBasketView.as_view(), name='basket_delete'),
    path('basket/<int:pk>/confirm_delete/', ConfirmDeleteProductInBasketView.as_view(), name='basket_confirm_delete'),

]

