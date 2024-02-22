from django.shortcuts import render, redirect


def bag(request):
    """
    A view to return the shopping bag page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Adds the selected quantity of items to the bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
