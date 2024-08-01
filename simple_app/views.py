from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .filters import ProductFilter
from .forms import ProductForm
from .models import Product


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class ProductCreate(CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


# Представление удаляющее товар.

class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
#
#
# class ProductsList(ListView):
#     # Указываем модель, объекты которой мы будем выводить
#     model = Product
#     # Поле, которое будет использоваться для сортировки объектов
#     ordering = 'name'
#     # Указываем имя шаблона, в котором будут все инструкции о том,
#     # как именно пользователю должны быть показаны наши объекты
#     template_name = 'products.html'
#     # Это имя списка, в котором будут лежать все объекты.
#     # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
#     context_object_name = 'products'
#     paginate_by = 2  # вот так мы можем указать количество записей на странице
#
#     def __init__(self, **kwargs):
#         super().__init__(kwargs)
#         self.filterset = None
#
#     def get_context_data(self, **kwargs):
#         # С помощью super() мы обращаемся к родительским классам
#         # и вызываем у них метод get_context_data с теми же аргументами,
#         # что и были переданы нам.
#         # В ответе мы должны получить словарь.
#         context = super().get_context_data(**kwargs)
#         # К словарю добавим текущую дату в ключ 'time_now'.
#         context['time_now'] = datetime.utcnow()
#         # Добавим ещё одну пустую переменную,
#         # чтобы на её примере рассмотреть работу ещё одного фильтра.
#         context['next_sale'] = "Распродажа в среду!"
#         context['filterset'] = self.filterset
#         return context
#
#
# class ProductDetail(DetailView):
#     # Модель всё та же, но мы хотим получать информацию по отдельному товару
#     model = Product
#     # Используем другой шаблон — product.html
#     template_name = 'product.html'
#     # Название объекта, в котором будет выбранный пользователем продукт
#     context_object_name = 'product'
#
#     # def multiply(request):
#     #     number = request.GET.get('number')
#     #     multiplier = request.GET.get('multiplier')
#     #
#     #     try:
#     #         result = int(number) * int(multiplier)
#     #         html = f"<html><body>{number}*{multiplier}={result}</body></html>"
#     #     except (ValueError, TypeError):
#     #         html = f"<html><body>Invalid input.</body></html>"
#     #
#     #     return HttpResponse(html)
#
#     def create_product(request):
#         form = ProductForm()
#
#         if request.method = 'POST':
#             form = ProductForm()
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect('/products')
#
#         return render(request, 'product_edit.html', {'form': form})
