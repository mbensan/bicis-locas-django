from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Biker


def index(request):
    return render(request, 'index.html')


def index_ajax(request):
    return render(request, 'index_ajax.html')


def save_biker(request):
    errors = Biker.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    print(errors)
    return redirect('/')


def new_ajax(request):
    errors = Biker.objects.basic_validator(request.POST)
    msgs = []
    
    if len(errors) > 0:
        for key, value in errors.items():
            msgs.append(value)
    
    if len(msgs) > 0:
        return JsonResponse({'msgs': msgs}, status=400)

    return JsonResponse({'status': 'OK'}, status=200)


def second(request, name):
    return HttpResponse('Hola ' + name)

