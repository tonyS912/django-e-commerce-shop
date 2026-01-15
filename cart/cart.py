from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self, request):
        """
        Initialize the cart.

        Args:
            request (_type_): session cookie
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart
