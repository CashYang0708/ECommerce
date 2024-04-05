from django.core.mail import send_mail
from django.shortcuts import render, redirect
from store.form import ContactForm
from django.template.loader import render_to_string


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]
            content = form.cleaned_data["content"]

            html = render_to_string(
                "reserve.html",
                {
                    "email": email,
                    "date": date,
                    "time": time,
                    "content": content,
                },
            )

            print("the form was valid")

            send_mail(
                "預約",
                "This is the message",
                "lindacheng1111@gmail.com",
                [email],
                html_message=html,
            )

            return redirect("reserve")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
