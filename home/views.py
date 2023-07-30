from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def home(request):
    profile = Profile.objects.filter(user = request.user).first()
    expenses = Expense.objects.filter(user = request.user)
    if request.method == 'POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')

        expense = Expense(name=text, amount= amount, user=request.user)
        expense.save()       

        if (float(amount) >= 0):
            profile.balance -= float(amount)
            profile.expenses -=float(amount)

        else:
            pass
        profile.save()
        return redirect('/')
   
    context = {
        'profile' : profile,
        'expenses': expenses
        }
    return render(request, 'home.html' , context)