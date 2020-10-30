from django.shortcuts import render

from app.models import Profile, Expense
from app.views.profiles import create_profile


def index(request):
    if Profile.objects.exists():
        expenses = Expense.objects.all()
        profile = Profile.objects.all()[0]
        expenses_cost = sum(expense.price for expense in expenses)
        profile.budget_left = profile.budget - expenses_cost

        context = {
            'profile': profile,
            'expenses': expenses,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return create_profile(request)
