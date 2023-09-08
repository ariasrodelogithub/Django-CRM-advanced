from django.contrib import admin
from .models import *


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'last_name',
                    'dni',
                    'date_created',
                    'date_update',
                    'sexo',
                    'address',

                    )


admin.site.register(Client, ClienteAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'category',
                    'image',
                    'pvp',
                    )


admin.site.register(Product, ProductAdmin)
