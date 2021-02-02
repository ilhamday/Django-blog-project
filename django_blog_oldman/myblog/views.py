from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import CommentForm
from django.db.models import Q

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains = query)| # find with given query
            Q(description__icontains = query)
        ).distinct()
    
    context = {
        'queryset':queryset, 
    }

    return render(request, 'search_results.html', context)


def index(request):
    queryset = Post.objects.all()
    category_set = Category.objects.all()
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
        'category_set': category_set,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'index.html', context)

def blog(request, post_id):
    blog = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = blog # match the blog post, see above variable
            form.save()

            return redirect('blog_detail', post_id=post_id)

    context = {
        'blog': blog,
        'form': form,
    }
    return render(request, 'blog-detail.html', context)
    
def category_view(request, cats):
    # Post is a class in models.py | filter by title 
    category_post = Post.objects.filter(categories__title__contains=cats)
    category_set = Category.objects.all()
    context = {
        'category_set': category_set,
        'cats': cats,
        'category_post': category_post
    }
    return render(request, 'categories.html', context)