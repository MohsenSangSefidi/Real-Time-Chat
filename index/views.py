from django.shortcuts import render
from django.views import View


def index_view(request, *args, **kwargs):
    return render(request, 'index.html', {})
