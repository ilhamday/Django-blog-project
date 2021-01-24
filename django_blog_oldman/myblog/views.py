from django.shortcuts import render
from .models import *


def index(request):
    queryset = Post.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'index.html', context)

def blog(request):
    return render(request, 'blog-detail.html')
    
