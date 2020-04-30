from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def view_cart(request):
    """
    A view that renders the cart contents
    """
    return render(request, 'cart.html')


@login_required
def add_to_cart(request, id):
    """
    Add the listing to cart
    """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_item(request, id):
    """
    Delete item from cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity <= 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    messages.success(request, "Item successfully deleted from your cart")
    return redirect(reverse('view_cart'))
