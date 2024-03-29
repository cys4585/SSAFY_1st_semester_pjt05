from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Movie
from .forms import MovieForm

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()

    context = {
        'form': form
    }
    return render(request, 'movies/form.html', context)


@require_safe
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        'movie': movie,
    }
    
    return render(request, 'movies/detail.html', context)

@require_http_methods(['POST', 'GET'])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form':form,
        'movie':movie
    }
    return render(request, 'movies/form.html', context)

@require_POST
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movies:index')