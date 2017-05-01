from django.db import models
from django.core.urlresolvers import reverse


class CSQuote(models.Model):
    author = models.CharField(max_length=50, )
    quote_text = models.CharField(max_length=1000, )


    def __str__(self):
        return self.author + ": " + self.quote_text

    # def get_absolute_url(self):
        # return "http://localhost:8000/quotes/searchcs/{author}".format(author=self.author)


class StoicQuote(models.Model):
    author = models.CharField(max_length=50, )
    quote_text = models.CharField(max_length=1000, )


    def __str__(self):
        return self.author + ": " + self.quote_text
