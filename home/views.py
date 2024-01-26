from django.shortcuts import render

# Create your views here.
from .models import TopLooser
from django.http import HttpResponse


def home(request):
    # return HttpResponse("Hello world!")
    data = TopLooser.objects.all()

    # Pass the data to the template
    context = {'data': data}
    return render(request, 'index.html', context)
