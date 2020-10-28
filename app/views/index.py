from django.shortcuts import render

from app.forms.profiles import ProfileForm
from app.models import Profile


def index(request):
    if Profile.objects.exists():
        pass
    else:
        context = {
            'form': ProfileForm(),
        }

        return render(request, 'home-no-profile.html', context)
