from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout


def sign_up(request):
    """
    Task:
    - if this is a POST request we need to process the form data
    - create a form instance and populate it with data from the request
    - check whether it's valid
    - if a GET (or any other method) we'll create a blank form
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('movies:home'))
    # Return an 'invalid login' error message.
    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'users/logout.html')
