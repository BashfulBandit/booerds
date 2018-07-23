from django import forms

# Create your forms here.
class PaymentChoicesForm(forms.Form):
    CREDIT_CARD = 'CC'
    CASH = 'CA'
    CHECK = 'CH'
    PAYMENT_CHOICES = (
        (CREDIT_CARD, 'CREDIT CARD'),
        (CASH, 'CASH'),
        (CHECK, 'CHECK'),
    )
    payment_options = forms.ChoiceField(
        required=False,
        choices=PAYMENT_CHOICES,
    )

class PaymentInfoForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=True,
    )
    number = forms.CharField(
        max_length=16,
        label='Credit Card Number',
        required=True,
    )
    expiration_date = forms.DateField(
        required=True,
    )
    CVV = forms.CharField(
        max_length=3,
        label='CVV',
        required=True,
    )
#
# class CheckForm(form.Form):
#
# class CashForm(form.Form):
