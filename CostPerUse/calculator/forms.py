from django import forms

class CalcForm(forms.Form):
    product = forms.CharField(label='Покупка:', max_length=200)
    cost = forms.CharField(label='Цена:')
    times_per_month = forms.IntegerField(label='Сколько раз в месяц:')
    months_per_year = forms.IntegerField(label='Сколько месяцев в год:')
    years = forms.IntegerField(label='Сколько лет:')


