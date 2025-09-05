from django import forms


class QuoteForm(forms.Form):
    your_quote = forms.CharField(label="Your quote", max_length=100)
    quote_source = forms.CharField(label="Quote source", max_length=100)
    weight = forms.IntegerField(label="Weight")
