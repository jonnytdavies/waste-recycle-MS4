from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_trunk(request):
    """
    A view that renders the trunk contents
    """
    return render(request, 'trunk.html')


def add_to_trunk(request, id):
    """
    Add the listing to trunk
    """
    quantity = int(request.POST.get('quantity'))

    trunk = request.session.get('trunk', {})
    trunk[id] = trunk.get(id, quantity)

    request.session['trunk'] = trunk
    return redirect(reverse('index'))


def delete_item(request, id):
    """
    Delete item from trunk
    """
    quantity = int(request.POST.get('quanitity'))
    trunk = request.session.get('trunk', {})

    if quantity > 0:
        trunk[id] = quantity
    else:
        trunk.pop(id)

    request.session['trunk'] = trunk
    return redirect(reverse('view_trunk'))
