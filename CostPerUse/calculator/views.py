from django.shortcuts import render, redirect
from .forms import CalcForm


def calculator(request):
    form = CalcForm()

    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            cost_per_use = round(form.cleaned_data.get('cost') / (form.cleaned_data.get('years') * form.cleaned_data.get(
                'months_per_year') * 30.4 / 7 * form.cleaned_data.get('times_per_week')), 1)
            print(cost_per_use)

    context = {
        'form': form,
        # 'cost_per_use': cost_per_use,
    }
    return render(request, 'calculator/calculator.html', context)

    # return render(request, 'calculator/calculator.html')
