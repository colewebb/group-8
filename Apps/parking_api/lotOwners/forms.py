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

class Login(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class TransferBalance(forms.Form):
    c = [('bank', 'My Bank Account'),("debit", "My debit card")]
    transferAmount = forms.FloatField(label="How much do you want to transfer?")
    transferLocation = forms.CharField(label="Where do you want to transfer to?", widget=forms.Select(choices=c))

class AssociateWithEvent(forms.Form):
    openTime = forms.TimeField(label="What time does your lot open?")
    closeTime = forms.TimeField(label="What time does your lot close?")
    costSmall = forms.FloatField(label="How much will you charge for a small spot?")
    costMedium = forms.FloatField(label="How much will you charge for a medium spot?")
    costLarge = forms.FloatField(label="How much will charge for a large spot?")
    capSmallActual = forms.IntegerField(label="How many small spots will you have available for this event?")
    capMediumActual = forms.IntegerField(label="How many medium spots will you have available for this event?")
    capLargeActual = forms.IntegerField(label="How many large spots will you have available for this event?")
    