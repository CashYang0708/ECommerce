from django.shortcuts import render
from store.models import Order
from django.views import View

class OrderView(View):
    def get(self, request):
        member=request.session.get('customer')
        orders=Order.get_orders_by_member(member)
        print(orders)
        return render(request, 'orders.html',{'orders':orders})