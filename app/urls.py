from django.urls import path

from app.views.categories.views import CategoryListView, CategoryCreateView


urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('category-list/', CategoryListView.as_view(), name='category-list'),
    path('create-category/', CategoryCreateView.as_view(), name='create-category'),

]
