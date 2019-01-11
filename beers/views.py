from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from beers.models import Beer, Company, SpecialIngredient


def beer_list_view(request):

    beer_list = Beer.objects.all()
    beer_list_counter = beer_list.count()
    #print("beer_list_counter",beer_list_counter)

    #print("exists?",beer_list.filter(id=1))

    #print("exists?", beer_list.filter(id=1).exists())
    #company = Company.objects.create(name="co", tax_number=45678)
    #Beer.objects.create(name="Broma",company=company)SWSSSS

    company = Company.objects.get(pk=2)
    #print(beer_list.filter(company__name__startswith="C",abv__gte=5))

    #O lógico
    #print(beer_list.filter( Q(company__name__startswith="C") | Q(abv__gte=5)))

    #print(Beer.objects.filter(pk=4).first().delete())

    """for beer in company.beers.all():
        print(beer)
        beer.abv = 4.81
        beer.save()"""

    #beer = Beer.objects.filter(pk__in=[1,2,3,4,5]).first()
    beer = Beer.objects.raw("SELECT * FROM beers_beer")
    print("Contenido de la variable beer")
    print(beer)

    print("Nombres obtenidos del QuerySet definido anteriormente")
    for beer in beer:
        print(beer.name)
    #ingredient = SpecialIngredient.objects.get(pk=1)
    #beer.special_ingredients.add(ingredient)


    #print(Beer.image.url)

    #special = SpecialIngredient(name="Romero")
    #special.save()
    beer_count = beer_list.count()
    print(beer_count)


    context = {
        'beer_list': Beer.objects.all(),
        'beer_count': beer_list.count(),
    }
    return render(request,'beer_list.html',context)


def beer_detail_view(request,pk):
    print("user",request.user)
    print("GET",request.is_ajax())
    context = {
        'beer' : Beer.objects.get(pk = pk)
    }
    return render(request, 'beer_detail.html', context)