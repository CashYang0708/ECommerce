from django.shortcuts import redirect
from django.views import View
from store.models import Product, Order, Member


class CheckOut(View):
    def post(self, request):
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        customer = request.session.get("customer")
        cart = request.session.get("cart")
        products = Product.get_Product_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(
                member=Member(id=customer),
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                quantity=cart.get(str(product.id)),
            )
            order.save()
        request.session["cart"] = {}

        return redirect("cart")
