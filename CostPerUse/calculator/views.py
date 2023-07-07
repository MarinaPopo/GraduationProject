from django.shortcuts import render, redirect
from .forms import CalcForm


def calculator(request):
    form = CalcForm(request.GET)
    cost_per_use = 0
    product = str
    times = 0
    if form.is_valid():
        times = int(form.cleaned_data.get('years') * form.cleaned_data.get('months_per_year') * (30.4 / 7) * \
                    form.cleaned_data.get('times_per_week'))
        cost_per_use = round(int(form.cleaned_data.get('cost')) / times, 1)
        product = form.cleaned_data.get('product').lower()
    print(cost_per_use)
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

    # return render(request, 'calculator/calculator.html')
