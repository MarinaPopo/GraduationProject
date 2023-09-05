from django.shortcuts import render, redirect
from .forms import CalcForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
import pymorphy3


def calculator(request):
    form = CalcForm(request.GET)
    cost_per_use = 0
    product = str
    times = 0

    if form.is_valid():
        times = int(form.cleaned_data.get('years') * form.cleaned_data.get('months_per_year') *
                    form.cleaned_data.get('times_per_month'))
        cost_per_use = round(int(form.cleaned_data.get('cost')) / times, 1)
        product = form.cleaned_data.get('product')
        morph = pymorphy3.MorphAnalyzer()
        one = morph.parse(product)[0]
        product = one.inflect({'accs'}).word

    if times % 10 == 2 or times % 10 == 3 or times % 10 == 4:
        variant = 'раза'
    else:
        variant = 'раз'

    context = {
        'form': form,
        'cost_per_use': cost_per_use,
        'product': product,
        'times': times,
        'variant': variant,
    }
    return render(request, 'calculator/calculator.html', context)


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'calculator/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('calculator')
            except IntegrityError:
                return render(request, 'calculatorcalculator/signupuser.html', {'form': UserCreationForm(),
                                                                                'error': 'Такое имя пользователя уже существует.'})
        else:
            return render(request, 'calculator/signupuser.html', {'form': UserCreationForm(),
                                                                  'error': 'Пароли не совпадают.'})


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('calculator')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'calculator/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'calculator/loginuser.html', {'form': AuthenticationForm()},
                          {'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('calculator')
