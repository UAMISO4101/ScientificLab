from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    context = {'mensaje': 'Hola Mundo'}
    return render(request, 'laboratorio/index.html', context)
    #return HttpResponse("Hello, world. You're at the polls index.")
