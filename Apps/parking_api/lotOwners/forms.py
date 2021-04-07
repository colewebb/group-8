from django import forms

class NewLotForm(forms.Form):
    lotName = forms.CharField(label="Name of lot:")
    lotAddress = forms.CharField(label="Lot address:", widget=forms.Textarea)
    smallSpotCount = forms.IntegerField(label="How many small spots do you have?")
    smallSpotCost = forms.FloatField(label="How much will you charge for a small spot?")
    mediumSpotCount = forms.IntegerField(label="How many medium spots do you have?")
    mediumSpotCost = forms.FloatField(label="How much will you charge for a medium spot?")
    oversizeSpotCount = forms.IntegerField(label="How many oversize spots do you have?")
    oversizeSpotCost = forms.FloatField(label="How much will you charge for an oversize spot?")

class ModifyLotForm(forms.Form):
    lotName = forms.CharField(label="Name of lot:")
    lotAddress = forms.CharField(label="Lot address:", widget=forms.Textarea)
    smallSpotCount = forms.IntegerField(label="How many small spots do you have?")
    smallSpotCost = forms.FloatField(label="How much will you charge for a small spot?")
    mediumSpotCount = forms.IntegerField(label="How many medium spots do you have?")
    mediumSpotCost = forms.FloatField(label="How much will you charge for a medium spot?")
    oversizeSpotCount = forms.IntegerField(label="How many oversize spots do you have?")
    oversizeSpotCost = forms.FloatField(label="How much will you charge for an oversize spot?")
    delete = forms.BooleanField(label="Delete?")

class Login(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class TransferBalance(forms.Form):
    transferAmount = forms.FloatField(label="How much do you want to transfer?")
    transferLocation = forms.CharField(label="Where do you want to transfer to?", widget=forms.Select(choices=[('bank', 'My Bank Account'),("debit", "My debit card")]))