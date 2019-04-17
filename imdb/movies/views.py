from django.shortcuts import render, reverse, get_object_or_404, HttpResponseRedirect
from .forms import MovieForm, ActorForm, AwardForm
from .models import Movies, Actors, Awards
from django.contrib.auth.decorators import login_required
from .models import Comments
from django.contrib.contenttypes.models import ContentType


@login_required
def index(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = MovieForm()
    contents = {
        "form": form,
        "movies_user": Movies.objects.all(),
        "user": request.user
    }
    return render(request, 'movies/index.html', contents)


@login_required
def view_movie(request, id):
    movie = get_object_or_404(Movies, id=id)
    kind_type = ContentType.objects.get(model='movies')
    if request.method == "POST":
        Comments.objects.create(text=request.POST['comment'],
                                author=request.user,
                                content_type=kind_type,
                                object_id=movie.id)
    comments = Comments.objects.filter(
        content_type=kind_type, object_id=movie.id)

    contents = {
        "movie": movie,
        "actors": ", ".join(map(str, movie.actors.all())),
        "comments": comments,
        "user": request.user
    }
    return render(request, 'movies/view_movie.html', contents)


@login_required
def update_movie(request, id):
    instance = get_object_or_404(Movies, id=id)
    form = MovieForm(request.POST or None,
                     request.FILES or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('movies:home'))
    contents = {
        "movie": Movies.objects.get(id=id),
        "form": form,
        "user": request.user
    }
    return render(request, 'movies/update_movie.html', contents)


@login_required
def delete_movie(request, id):
    movie = get_object_or_404(Movies, id=id)
    if request.method == "POST":
        movie.delete()
        return HttpResponseRedirect(reverse('movies:home'))
    contents = {
        "movie": movie,
        "user": request.user
    }
    return render(request, 'movies/delete_movie.html', contents)


@login_required
def view_actor(request, id):
    actor = get_object_or_404(Actors, id=id)
    kind_type = ContentType.objects.get(model='actors')
    if request.method == "POST":
        Comments.objects.create(text=request.POST['comment'],
                                author=request.user,
                                content_type=kind_type,
                                object_id=actor.id)
    comments = Comments.objects.filter(
        content_type=kind_type, object_id=actor.id)
    contents = {
        "actor": actor,
        "movies": ", ".join(map(str, actor.movies_set.all())),
        "comments": comments,
        "user": request.user
    }
    return render(request, 'movies/view_actor.html', contents)


@login_required
def update_actor(request, id):
    actor = get_object_or_404(Actors, id=id)
    form = ActorForm(request.POST or None,
                     request.FILES or None, instance=actor)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('movies:actors'))
    contents = {
        "actor": actor,
        "form": form,
        "user": request.user
    }
    return render(request, 'movies/update_actor.html', contents)


@login_required
def delete_actor(request, id):
    actor = get_object_or_404(Actors, id=id)
    if request.method == "POST":
        actor.delete()
        return HttpResponseRedirect(reverse('movies:actors'))
    contents = {
        "actor": actor,
        "user": request.user
    }
    return render(request, 'movies/delete_actor.html', contents)


@login_required
def view_actors(request):
    if request.method == 'POST':
        form = ActorForm(request.POST or None)
        if form.is_valid():
            form.save()
    form = ActorForm()
    contents = {
        "form": form,
        "actors_user": Actors.objects.all(),
        "user": request.user
    }
    return render(request, 'movies/actors.html', contents)


@login_required
def view_awards(request):
    if request.method == "POST":
        print(request.POST)
        form = AwardForm(request.POST)
        if form.is_valid():
            form.save()
            print('.....saving')
    form = AwardForm()
    contents = {
        "form": form,
        "user": request.user,
        "movies_award": Awards.objects.filter(kind="movie"),
        "actors_award": Awards.objects.filter(kind="actor"),
    }
    return render(request, 'movies/awards.html', contents)


@login_required
def update_comment(request, id):
    comment = get_object_or_404(Comments, id=id)
    if request.method == "POST" and request.POST.get('comment'):
        comment.text = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.POST['form_url'])
    contents = {
        "comment": comment,
        "form_url": request.POST['form_url'],
        "user": request.user
    }
    return render(request, 'movies/update_comment.html', contents)


@login_required
def delete_comment(request, id):
    comment = Comments.objects.get(id=id)
    comment.delete()
    return HttpResponseRedirect(request.POST['form_url'])
