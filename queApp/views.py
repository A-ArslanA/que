from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, View
from django.db.models import Q      #search
from .forms import AddGenreForm, AddViewForm, NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def homePage(request):
    return render(request, "user/banner.html")

def topViews(request):
    view = View.objects.all().order_by("-rating")[:1]
    views = View.objects.all().order_by("-rating")[:10]
    return render(request, "user/top-views.html", {
        'view': view,
        'views': views
    })

def allViews(request, slug=None):
    genre = None
    views = View.objects.all()
    genres = Genre.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        views = View.objects.filter(Q(viewName__icontains=searchData) | Q(description__icontains=searchData))
    else:
        views = View.objects.all()
    if slug:
        genre = get_object_or_404(Genre, slug=slug)
        views = views.filter(genre=genre)
    return render(request, "user/all-views.html", {
        'views': views,
        'genres': genres,
        'genre': genre
    })

def viewDetail(request, pk):
    view = get_object_or_404(View, pk=pk)
    return render(request, "user/view-detail.html", {
        'view': view
    })

def addViews(request):
    if request.method == "POST":
        form = AddViewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("allViews")
    else:
        form = AddViewForm()

    return render(request, "admin/add-view.html", {
        'form': form
    })

def addGenre(request):
    if request.method == "POST":
        form = AddGenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("allViews")
    else:
        form = AddGenreForm()

    return render(request, "admin/add-genre.html", {
        'form': form
    })

def signUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = NewUserForm()
    return render(request, "auth/sign-up.html", {
        'form': form
    })

def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("topViews")
    else:
        form = AuthenticationForm()
    return render(request, "auth/login.html", {
        'form': form
    })

def logoutUser(request):
    logout(request)
    return redirect("homePage")




