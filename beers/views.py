from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from beers.models import Beer


def beer_list_view(request):
    context = {
        'beer_list': Beer.objects.all()
    }
    return render(request,'beer_list.html',context)


def beer_detail_view(request,pk):
    print("user",request.user)
    print("GET",request.is_ajax())
    context = {
        'beer' : Beer.objects.get(pk = pk)
    }
    return render(request, 'beer_detail.html', context)