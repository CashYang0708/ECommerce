from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models import Member
from django.views import View
from store.models import Product


class Cart(View):
    def get(self, request):
        ids = list(request.session.get("cart").keys())
        products = Product.get_Product_by_id(ids)
        print(products)
        return render(request, "cart.html", {"products": products})
