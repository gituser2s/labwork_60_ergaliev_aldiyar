from django.contrib import admin
from webapp.models import Product, Basket

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'count', 'price', 'photo', 'created_at')
    list_filter = ('id', 'title', 'description', 'category', 'count', 'price', 'photo', 'created_at')
    search_fields = ('title', 'description', 'category', 'count', 'price', 'photo',)
    fields = ('title', 'description', 'category', 'count', 'price', 'photo', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at', 'deleted_at', 'is_deleted')


admin.site.register(Product, ProductAdmin)


class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'count')
    list_filter = ('id', 'product', 'count')
    search_fields = ('product', 'count')
    fields = ('product', 'count')
    readonly_fields = ('id',)


admin.site.register(Basket, BasketAdmin)
