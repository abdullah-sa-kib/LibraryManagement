from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post']


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally log the user in immediately after signing up:
            login(request, user)
            return redirect('book_list')  # or wherever you want
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
