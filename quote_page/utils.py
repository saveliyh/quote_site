from .models import Quote, TableQuote
from numpy.random import choice


def get_random(quotes):
    weights = [weight[0] for weight in quotes.values_list("weight")]
    weights = [weight / sum(weights) for weight in weights]
    return choice(quotes, 1, p=weights)[0]


def check_data(data):
    print(f"checking: {data}")
    return (
        not Quote.objects.filter(quote=data["your_quote"]).exists()
        and len(Quote.objects.filter(source=data["quote_source"])) < 3
    )


def get_statistics():
    quotes = TableQuote.objects.order_by("-likes")
    ids = []
    i = 0
    for quote in quotes[:10]:
        i += 1
        ids.append(quote.id)
        quote.position = i
        quote.save()
    table = TableQuote.objects.filter(id__in=ids).order_by("position")

    return {"quotes": table}
