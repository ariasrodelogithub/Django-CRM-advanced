from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from app.models import Category
from app.forms import CategoryForm


class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'listado de categorías'  # pasas por contexto lo que quieras
        context['create_url'] = reverse_lazy('create-category')
        return context


class CategoryCreateView(CreateView):
    model = Category
    template_name = "categories/category_create.html"
    form_class = CategoryForm
    success_url = reverse_lazy('category-list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST.get('action')
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No hay acción seleccionada'

        except Exception as e:
            data['error'] = f"Error: {e}"
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Crear categoría'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('category-list')
        return context
