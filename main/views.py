# Импорт необходимых модулей
from django.shortcuts import render, redirect, HttpResponseRedirect
from main import models
from main import forms
from django.db.models import Q
from django.urls import reverse
from .models import Product

# Основная функция для отображения главной страницы
def index(request):
    # Проверка аутентификации пользователя
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    # Получение популярных и новых продуктов
    popular_products = Product.objects.filter(popular=True)
    new_products = Product.objects.filter(new=True)
    
    # Получение всех категорий продуктов
    categories = models.ProductCategory.objects.all()
    
    # Подготовка контекста для передачи в шаблон
    context = {
        'popular_products': popular_products,
        'new_products': new_products,
        'categories': categories,
    }

    # Отображение главной страницы с переданным контекстом
    return render(request, 'main/index.html', context)

# Функция для отображения страницы "О нас"
def about(request):
    return render(request, "main/about.html")

# Функция для отображения профиля пользователя
def profile(request):
    return render(request, "main/profile.html")

# Функция для отображения страницы корзины
def cart(request):
    return render(request, "main/cart.html")

# Функция для отображения страницы заказов
def orders(request):
    return render(request, "main/orders.html")

# Функция для отображения страницы настроек
def settings(request):
    return render(request, "main/settings.html")

# Функция для отображения страницы продукта по идентификатору
def product_index(request, id):
    product = models.Product.objects.filter(pk=id).first()
    return render(request, 'main/product_index.html', context={'product': product})

# Функция для добавления нового продукта
def add_product(request):
    # Создание экземпляра формы для добавления продукта
    form = forms.ProductForm()

    if request.method == "POST":
        # Обработка данных из POST-запроса для добавления продукта
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            # Обработка случая, когда форма неверна
            return render(request, 'main/add_product.html', context={'form': form})

    return render(request, 'main/add_product.html', context={'form': form})

# Функция для поиска продуктов
def search_products(request):
    query = request.GET.get('q')

    if query:
        # Использование Q-объектов для выполнения поиска по нескольким полям
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(category__name__exact=query)
        )
    else:
        # Если запрос пуст, получаем все продукты
        products = Product.objects.all()

    # Отображение результатов поиска
    return render(request, 'main/search_results.html', {'products': products, 'query': query})

# Функция для отображения страницы с категориями продуктов
def categories(request):
    # Получение всех продуктов и категорий
    products = models.Product.objects.all()
    categories = models.ProductCategory.objects.all()

    # Подготовка контекста для передачи в шаблон
    context = {
        'products': products,
        'categories': categories,
    }
    
    # Отображение страницы с категориями
    return render(request, 'main/categories.html', context)
