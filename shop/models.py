from django.db import models


# Represents a product category; used for navigation and SEO-friendly URLs.
class Category(models.Model):
    # Human-readable label shown in UI.
    name = models.CharField(max_length=200)
    # URL identifier (e.g. /category/<slug>/). Must be unique to avoid routing ambiguity.
    slug = models.SlugField(max_length=200, unique=True)

    # Django model metadata:
    # - query defaults (ordering, get_latest_by)
    # - database-level options (indexes, constraints)
    # - admin/UI labels (verbose_name, verbose_name_plural)
    class Meta:
        ordering = ["name"]  # Default sort order for category querysets.
        indexes = [models.Index(fields=["name"])]
        verbose_name = "category"
        verbose_name_plural = "categories"

    # Readable representation in admin dropdowns, logs, etc.
    def __str__(self):
        return self.name


# Represent a product.
class Product(models.Model):
    """
    A sellable product in the storefront.

    - Belongs to a category (used for navigation and filtering).
    - `name` is the human-readable label shown in the UI.
    - `slug` is a URL-friendly identifier (readable URLs / SEO).
    - `available` allows hiding products without deleting them.
    - `created` / `updated` are audit timestamps.
    """

    category = models.ForeignKey(
        Category,
        related_name="products",  # reverse access: category.products.all()
        on_delete=models.CASCADE,  # deleting a category deletes its products too
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(
        upload_to="products/%Y/%m/%d", blank=True
    )  # image is optional (blank=True)
    description = models.TextField(blank=True)  # description is optional (blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Django model metadata:
    # - query defaults (ordering, get_latest_by)
    # - database-level options (indexes, constraints)
    # - admin/UI labels (verbose_name, verbose_name_plural)
    class Meta:
        ordering = ["name"]  # Default sort order for product querysets.
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(
                fields=["-created"]
            ),  # hyphen before created, index in descending order
        ]

    # Readable representation in admin dropdowns, logs, etc.
    def __str__(self):
        return self.name
