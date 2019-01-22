from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from beers.forms import CompanyForm, LoginPruebaForm
from beers.mixins import AddMyBirthdayToContextMixin
from beers.models import Beer, Company, SpecialIngredient

"""@login_required
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

    for beer in company.beers.all():
        print(beer)
        beer.abv = 4.81
        beer.save()

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
    return render(request,'beer_list.html',context)"""

class BeerListView(ListView):
    model = Beer

    def get_queryset(self):
        return Beer.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        beer_list = Beer.objects.all()
        beer_count = beer_list.count()
        context = {
            'lista_cervezas': Beer.objects.all(),
            'contador_cervezas': beer_list.count(),
        }
        return context


"""def beer_detail_view(request,pk):
    print("user",request.user)
    print("GET",request.is_ajax())
    context = {
        'beer' : Beer.objects.get(pk = pk)
    }
    return render(request, 'beer_detail.html', context)"""

class BeerDetailView(DetailView):
    model = Beer



def company_edit_old(request,pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        print("POST",request.POST)
        form = CompanyForm(request.POST)
        if form.is_valid():
            company.name = form.cleaned_data['name']
            company.tax_number = form.cleaned_data['tax_number']
            company.save()
    else:
        form = CompanyForm(initial={
            'name': company.name,
            'tax_number': company.tax_number
        })
    context = {
        'form':form
    }
    return render(request,'company/company_form.html',context)

def company_edit(request,pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
    else:
        form = CompanyForm(instance=company)
    context = {
        'form':form
    }
    return render(request,'company/company_form.html',context)


class CompanyEditView(UpdateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list-view')

class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list-view')


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company/company_detail.html'

class CompanyListView(ListView):
    model = Company

def error404(request):
    return render(request,'/templates/404.html')

class LoginPrueba(LoginView):
    authentication_form = LoginPruebaForm