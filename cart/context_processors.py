"""Context Processors
they make things global like shopping carts
"""

from .cart import Cart


def cart(request):
    return {"cart": Cart(request)}
