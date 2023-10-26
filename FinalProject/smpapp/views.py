from django.http import HttpResponse
from django.shortcuts import render
from.models import place
# Create your views here.



def demo(request):
    obj = place.objects.all()

    return render(request, "home.html", {'result': obj})
# def addition(request):
#     x = int(request.GET['txt'])
#     y = int(request.GET['txt1'])
#     res = x+y
#     return render(request, 'result.html', {"result":res})