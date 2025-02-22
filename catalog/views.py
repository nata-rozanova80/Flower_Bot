# catalog/views.py
from django.shortcuts import render
from .models import Product
from django.shortcuts import redirect
from django.contrib import messages

from django.shortcuts import get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

# def product_list(request):
#     print("product_list view was called")
#     products = Product.objects.all()
#
#     return render(request, 'catalog/product_list.html', {'products': products})

def product_list(request):
    print("product_list view was called")
    # Используем prefetch_related для оптимизации запросов и загрузки отзывов
    products = Product.objects.prefetch_related('reviews').all()
    return render(request, 'catalog/product_list.html', {'products': products})

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, "Ваш отзыв успешно добавлен!")
            return redirect('product_list')
    else:
        form = ReviewForm()

    return render(request, 'catalog/add_review.html', {'form': form, 'product': product})


def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        if not product_id:
            messages.error(request, "Не удалось добавить товар в корзину.")
            return redirect("product_list")

        # Получаем корзину из сессии (если её нет, создаём пустую)
        cart = request.session.get("cart", {})

        # Проверяем, есть ли уже этот товар в корзине
        if product_id in cart:
            # Если товар уже есть, увеличиваем его количество
            cart[product_id] += 1
        else:
            # Если товара нет, добавляем его с количеством 1
            cart[product_id] = 1

        # Обновляем корзину в сессии
        request.session["cart"] = cart
        messages.success(request, "Товар успешно добавлен в корзину!")

    return redirect("product_list")

#Просмотр корзины должен стоять после других представлений

def view_cart(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    cart_items = []
    total = 0

    for product in products:
        quantity = cart.get(str(product.id)) or cart.get(product.id)  # Для надёжности
        quantity = int(quantity)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'catalog/view_cart.html', {'cart_items': cart_items, 'total': total})


