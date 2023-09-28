from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CalcForm(forms.Form):
    product = forms.CharField(label='Покупка', max_length=200)
    cost = forms.CharField(label='Цена')
    times_per_month = forms.IntegerField(label='Сколько раз в месяц')
    months_per_year = forms.IntegerField(label='Сколько месяцев в год')
    years = forms.IntegerField(label='Сколько лет')

    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control py-4'


class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control py-4'