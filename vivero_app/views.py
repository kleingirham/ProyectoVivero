from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Productor

# Create your views here.
'''def productor_detail(request, productor_id):
    productor = get_object_or_404(Productor, pk=productor_id)
    return render(request, 'vivero_app/productor_detail.html', {'productor': productor})'''