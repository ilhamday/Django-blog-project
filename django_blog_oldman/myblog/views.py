from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    queryset = Post.objects.all()

    # PAGINATION
    paginator = Paginator(queryset, 2) # from queryset, show 2 post per page | change the number if want to show more.
    
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'index.html', context)

def blog(request, post_id):
    blog = get_object_or_404(Post, pk=post_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog-detail.html', context)
    
