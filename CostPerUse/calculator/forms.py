from django import forms

class CalcForm(forms.Form):
    product = forms.CharField(label='Покупка:', max_length=200)
    cost = forms.IntegerField(label='Цена:')
    times_per_week = forms.IntegerField(label='Сколько раз в неделю:')
    months_per_year = forms.IntegerField(label='Сколько месяцев в год:')
    years = forms.IntegerField(label='Сколько лет:')

