from django.shortcuts import render
from .models import Pregunta
from django.http import JsonResponse
#from .corpus import tous
from .geminitools import procesar_preg


def enviar(request):  # Envia la respuesta del usuario y la guarda en BD
    if request.method == 'POST':
        userText = request.POST.get('userText')  # Obtiene el prompt desde JS
        procesar_preg(userText)
        return JsonResponse({'respuesta': userText})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def recibir(request):  # Obtiene la ultima respuesta de Gemini guardada en la BD
    if request.method == 'GET':
        ultimaRespuesta = Pregunta.objects.latest('id').parts
        return JsonResponse({'respuesta': ultimaRespuesta})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def renderizar_pagina(request):
    #tous()
    return render(request, "cerebro/res.html", {})


def borrar(request):
    return render(request, 'cerebro/borrar.html', {})