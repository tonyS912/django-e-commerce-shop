from django.shortcuts import get_object_or_404, render

# Import the domain models used by this view:
# - Category: for navigation and (optional) filtering
# - Product: the items shown in the storefront listing
from .models import Category, Product
from cart.forms import CartAddProductForm


# Create a view to list all the products.
def product_list(request, category_slug=None):
    """
    Product catalog listing view.

    Behavior:
    - Without a category slug: show all available products.
    - With a category slug: show only products that belong to that category.

    Template context:
    - categories: list of all categories (e.g. for a sidebar/menu)
    - category: the selected category (None if no filter is active)
    - products: queryset of products to display (only available ones)
    """

    # Selected category when browsing a specific category page.
    # Starts as None so the template can check "is a category filter active?"
    category = None
    # Used for category navigation on the page (e.g. sidebar).
    categories = Category.objects.all()

    # Base queryset for the storefront: never show unavailable products.
    # Note: further filters (like category) are applied on top of this.
    products = Product.objects.filter(available=True)

    # If a category slug is provided (e.g. from the URL), we are in "filtered listing" mode.
    if category_slug:
        # Resolve the category or return 404 if the slug does not exist.
        # (This prevents showing an empty page for a non-existent category.)
        # Important: get_object_or_404 needs lookup kwargs (usually slug=category_slug).
        category = get_object_or_404(Category, slug=category_slug)

        products = products.filter(category=category)

        # Render the catalog page with category navigation + (optionally filtered) product list.
    return render(
        request,
        "shop/product/list.html",
        {"category": category, "categories": categories, "products": products},
    )


# Create a view to get a detail for a products.
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        "shop/product/detail.html",
        {"product": product, "cart_product_form": cart_product_form},
    )
