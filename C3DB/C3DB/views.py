from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .forms import SignUpForm


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('register_done')

    else:
        form = SignUpForm()

    return render(request, 'registration/register.html', {'form': form})


class UserCreateDoneTV(TemplateView):

    template_name = 'registration/register_done.html'
