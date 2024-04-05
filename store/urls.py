from django.contrib import admin
from django.urls import path
from .views.home import Index, store
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.sendmail import index
from .views.decoration import DecorationView
from .views.orders import OrderView
from .views.checkout import CheckOut

from .auth import auth_middleware


urlpatterns = [
    path("", Index.as_view(), name="homepage"),
    path("store", store, name="store"),
    path("signup", Signup.as_view(), name="signup"),
    path("login", Login.as_view(), name="login"),
    path("logout", logout, name="logout"),
    path("cart", auth_middleware(Cart.as_view()), name="cart"),
    path("reserve", index, name="reserve"),
    path("decoration", auth_middleware(DecorationView.as_view()), name="decoration"),
    path("check-out", CheckOut.as_view(), name="checkout"),
    path("orders", auth_middleware(OrderView.as_view()), name="orders"),
]
