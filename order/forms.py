from django import forms



class UserNewOrderForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )
    count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'input-quantity'}),
        initial = 1
    )