from django.shortcuts import redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product
from webapp.forms import ProductForm


class ProductUpdateView(UpdateView):
    template_name = 'product_update.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')


class ProductConfirmDeleteView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        product.delete()
        return redirect('index')


class ProductDetail(DetailView):
    template_name = 'product.html'
    model = Product









