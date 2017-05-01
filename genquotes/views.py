from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import CSQuote, StoicQuote
from .forms import SearchForm

# Create your views here.

from django.http import HttpResponse

def home(request):
    form = SearchForm()
    if form.is_valid():
        print(form.cleaned_data)

    recent_quotes = CSQuote.objects.order_by('-pub_date')
    context = {
        'recent_quotes': recent_quotes,
        'form': form,
    }
    return render(request, 'genquotes/home.html', context)

def displaycs(request):
    #quote = get_object_or_404(Quote, pk=quote_id)
    randomcs = CSQuote.objects.order_by('?').first()

    context = {
        'randomcs': randomcs,
    }
    return render(request, 'genquotes/displaycs.html', context)

def displaystoic(request):
    #quote = get_object_or_404(Quote, pk=quote_id)
    randomstoic = StoicQuote.objects.order_by('?').first()
    context = {
        'randomstoic': randomstoic,

    }
    return render(request, 'genquotes/displaystoic.html', context)

def searchcs(request):
    error = ['Author not found.']
    authorquery = request.GET.get("author")
    csquotesby = CSQuote.objects.filter(author__iexact=authorquery)
    stoicquotesby = StoicQuote.objects.filter(author__iexact=authorquery)
    if (csquotesby):
        querylist = csquotesby
    elif (stoicquotesby):
        querylist = stoicquotesby
    if (len(authorquery) > 30):
        error.append('Search term must not exceed 30 characters.')
        error = ' '.join(error)
        return render(request, 'genquotes/home.html', {'error': error})
    if (len(authorquery) < 5):
        error.append('Search term must exceed 5 characters.')
        error = ' '.join(error)
        return render(request, 'genquotes/home.html', {'error': error})
    if not csquotesby and not stoicquotesby:
        #raise Http404("No quotes found")
        error.append('Please search again.')
        error = ' '.join(error)
        return render(request, 'genquotes/home.html', {'error': error})




    # csquotesby = get_list_or_404(CSQuote, author__iexact=authorquery)
    # stoicquotesby = get_list_or_404(StoicQuote, author__iexact=authorquery)
    context = {
        'results': querylist,
        'author': authorquery,
    }
    return render (request, 'genquotes/searchcs.html', context)
