from django import forms


class AsteroidsNeoWsForm(forms.Form):
    start_date = forms.DateField(label='Дата', widget=forms.DateInput(
        attrs = {'placeholder': 'YYYY-MM-DD',
                 'style': 'font-size: 25px;'}
    ))


class NeoLookupForm(forms.Form):
    id = forms.IntegerField(label='ID', widget=forms.NumberInput(
        attrs = {'placeholder': 'Введите ID',
                 'style': 'font-size: 25px;'}
    ))