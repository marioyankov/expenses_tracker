from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from app.forms.profiles import ProfileForm


def profile_index(request):
    pass


def create_profile(request):
    if request.method == 'GET':
        context = {
            'form': ProfileForm(),
        }

        return render(request, 'home-no-profile.html', context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    pass


def delete_profile(request):
    pass
