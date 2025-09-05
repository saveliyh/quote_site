from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Quote, TableQuote
from .forms import QuoteForm
from .utils import check_data, get_statistics, get_random
from django.contrib.auth import authenticate, login
import random


def add_quote(request):

    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if check_data(data):
                likes = random.randint(0, 100)
                quote = Quote(
                    quote=data["your_quote"],
                    source=data["quote_source"],
                    weight=data["weight"],
                    likes=likes,
                    dislikes=0,
                    views=0,
                )
                quote.save()
                table_quote = TableQuote(
                    position=0,
                    quote=data["your_quote"],
                    source=data["quote_source"],
                    likes=likes,
                )
                table_quote.save()
                print("success")
                return render(request, "quote_page/success_add.html", {"form": form})
            else:
                print("fail")
                return render(request, "quote_page/fail_add.html", {"form": form})
    else:
        form = QuoteForm()
    return render(request, "quote_page/add_quote.html", {"form": form})


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
        data = request.POST.get("data")
        quote, liked = data[:-1], data[-1]
        quote = Quote.objects.get(quote=quote)
        table_quote = TableQuote.objects.get(quote=quote)
        if liked == "1":
            table_quote.likes -= 1
            table_quote.save()
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
            table_quote.likes += 1
            table_quote.save()
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


def statistics(request):

    return render(
        request,
        "quote_page/stat.html",
        get_statistics(),
    )
