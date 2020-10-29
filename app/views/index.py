from django.shortcuts import render

from app.forms.profiles import ProfileForm
from app.models import Profile, Expense
from app.views.profiles import create_profile


def index(request):
    if Profile.objects.exists():
        context = {
            'profile': Profile.objects.all()[0],
            'expenses': Expense.objects.all(),
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return create_profile(request)
