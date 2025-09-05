from .models import Quote
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
    quotes = Quote.objects.order_by("-likes")[:10]

    return {
        "quotes": [
            {
                "quote": quote.quote,
                "source": quote.source,
                "likes": quote.likes,
            }
            for quote in quotes
        ]
    }
