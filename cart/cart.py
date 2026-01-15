from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self, request):
        """
        Initialize the cart.

        Args:
            request (_type_): Session cookie
        """
        self.session = request.session  # store current session
        cart = self.session.get(
            settings.CART_SESSION_ID
        )  # get cart from current session, if not available create empty
        if not cart:
            # save empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart  # create cart dictionary
