from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Quote
from .forms import QuoteForm
from .utils import check_data, get_statistics, get_random
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import random


@login_required
def add_quote(request):

    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if check_data(data):
                quote = Quote(
                    quote=data["your_quote"],
                    source=data["quote_source"],
                    weight=data["weight"],
                    likes=random.randint(0, 100),
                    dislikes=0,
                    views=0,
                )
                quote.save()
                print("success")
                return render(request, "quote_page/success_add.html", {"form": form})
            else:
                print("fail")
                return render(request, "quote_page/fail_add.html", {"form": form})
    else:
        form = QuoteForm()
    return render(request, "quote_page/add_quote.html", {"form": form})


@login_required
def random_quote(request):
    if request.method == "GET":
        quotes = Quote.objects.all()
        if quotes:
            quote = get_random(quotes)
            quote.views += 1
            quote.save()
            return render(
                request,
                "quote_page/random_quote_not_liked.html",
                {
                    "quote": quote.quote,
                    "source": quote.source,
                    "views": quote.views,
                    "likes": quote.likes,
                },
            )

        return render(
            request,
            "quote_page/random_quote_not_liked.html",
            {
                "quote": "Цитата из базы данных",
                "source": "Источник цитаты",
                "views": 10,
                "likes": 11,
            },
        )
    else:
        print(list(request.POST.items()))
        quote, liked = request.POST.get("data").split(" ")
        quote = Quote.objects.get(quote=quote)
        if liked == "1":
            quote.likes -= 1
            quote.save()
            return render(
                request,
                "quote_page/random_quote_not_liked.html",
                {
                    "quote": quote.quote,
                    "source": quote.source,
                    "views": quote.views,
                    "likes": quote.likes,
                },
            )
        else:
            quote.likes += 1
            quote.save()
            return render(
                request,
                "quote_page/random_quote_liked.html",
                {
                    "quote": quote.quote,
                    "source": quote.source,
                    "views": quote.views,
                    "likes": quote.likes,
                },
            )


@login_required
def statistics(request):

    return render(
        request,
        "quote_page/stat.html",
        get_statistics(),
    )


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/")
    else:
        return render(request, "quote_page/invalid_login.html")
