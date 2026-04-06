from django.shortcuts import render
from .models import Time

def lista_times(request):
    times = Time.objects.all().order_by('nome')
    return render(request, 'web/times.html', {'times': times})
