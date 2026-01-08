from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.product_list, name="product_list"),  # bspw.: Startseite
    path(
        "<slug:category_slug>/", views.product_list, name="product_list_by_category"
    ),  # bspw.: kleidung, technik
    path(
        "<int:id>/<slug:slug>/", views.product_detail, name="product_detail"
    ),  # bspw.: id/usb-stick-usb-c
]
