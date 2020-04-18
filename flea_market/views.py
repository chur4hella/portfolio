from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from .models import *


def index(request):
    categories = SectionProduction.objects.filter(type_category__exact=SectionProduction.CATEGORY)
    print(categories.count())
    return render(request, 'flea_market/flea_market_index.html', {
        'categories': categories,

    })


def detail(request, ad_id):
    return HttpResponse('Ad number {}'.format(ad_id))

