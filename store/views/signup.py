from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models import Member
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        postData = request.POST
        username = postData.get("username")
        password = postData.get("password")
        # validation
        value = {
            "username": username,
        }
        error_message = None

        member = Member(username=username, password=password)
        error_message = self.validatemember(member)

        if not error_message:
            member.password = make_password(member.password)
            member.register()
            return redirect("homepage")
        else:
            data = {"error": error_message, "values": value}
            return render(request, "signup.html", data)

    def validatemember(self, member):
        error_message = None
        # saving
        return error_message
