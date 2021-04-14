from django import forms

class NewLotForm(forms.Form):
    lotName = forms.CharField(label="Name of lot:")
    lotAddress = forms.CharField(label="Lot address:", widget=forms.Textarea)
    smallSpotCount = forms.IntegerField(label="How many small spots do you have?")
    mediumSpotCount = forms.IntegerField(label="How many medium spots do you have?")
    oversizeSpotCount = forms.IntegerField(label="How many oversize spots do you have?")

class ModifyLotForm(forms.Form):
    lotName = forms.CharField(label="Name of lot:")
    lotAddress = forms.CharField(label="Lot address:", widget=forms.Textarea)
    smallSpotCount = forms.IntegerField(label="How many small spots do you have?")
    mediumSpotCount = forms.IntegerField(label="How many medium spots do you have?")
    oversizeSpotCount = forms.IntegerField(label="How many oversize spots do you have?")
    delete = forms.BooleanField(label="Delete?", required=False)

class Login(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class TransferBalance(forms.Form):
    c = [('bank', 'My Bank Account'),("debit", "My debit card")]
    transferAmount = forms.FloatField(label="How much do you want to transfer?")
    transferLocation = forms.CharField(label="Where do you want to transfer to?", widget=forms.Select(choices=c))