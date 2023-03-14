from django.shortcuts import redirect, get_object_or_404, reverse, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, ListView
from webapp.models import Product, Basket
from webapp.forms import BasketForm


class BasketView(ListView):
    template_name = 'basket_index.html'
    model = Basket
    context_object_name = 'baskets'


class ProductInBasketView(CreateView):
    template_name = 'basket_add.html'
    model = Basket
    form_class = BasketForm

    def get_success_url(self):
        return reverse('basket_index')


class DeleteProductInBasketView(DeleteView):
    template_name = 'basket_confirm_delete.html'
    model = Basket
    success_url = reverse_lazy('basket_index')


class ConfirmDeleteProductInBasketView(TemplateView):
    template_name = 'basket_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = get_object_or_404(Product, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        basket = get_object_or_404(Basket, pk=kwargs['pk'])
        basket.delete()
        return redirect('basket_index')
