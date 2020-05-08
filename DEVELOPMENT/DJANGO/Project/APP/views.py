from django.shortcuts import render

# Create your views here.


def home(request):
        url = 'index.html'
        return render(request, url)