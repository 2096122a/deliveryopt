from django import forms
from delivery.models import Route, PostedItem, UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('driver', 'VehicleHeight', 'VehicleLength', 'VehicleWidth')




class PostedItemForm(forms.ModelForm):
    SenderName = forms.CharField(max_length=128, help_text="Username")
    itemName = forms.CharField(max_length=128, help_text="Item Name")
    pickUpAddress1 = forms.CharField(max_length=128, help_text="Pick Up Address")
    pickUpPostCode = forms.CharField(max_length=128, help_text="Pick Up Postcode")
    pickUpContactNumber = forms.IntegerField(help_text="Pick Up Contact Number")
    RecipientName = forms.CharField(max_length=128, help_text="Recipent Name")
    dropOffAddress1 = forms.CharField(max_length=128, help_text="Recipent Address")
    dropOffPostCode = forms.CharField(max_length=128, help_text="Recipent Postcode")
    dropOffContactNumber = forms.IntegerField(help_text="Recipent Contact Number")
    height = forms.IntegerField(help_text="Height in cm")
    length = forms.IntegerField(help_text="Length in cm")
    width = forms.IntegerField(help_text="Width in cm")
    weight = forms.IntegerField(help_text="Weight in Kg")
    date = forms.DateField(help_text="date, in dd/mm/yy")
    complete = forms.CharField(widget=forms.HiddenInput(), required=False)
    mslug = forms.CharField(widget=forms.HiddenInput(), required=False)


    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = PostedItem


class RouteForm(forms.ModelForm):
    driverName = forms.CharField(max_length=128, help_text="Please enter your name")
    start = forms.CharField(max_length=128, help_text="Starting City")
    end = forms.CharField(max_length=128, help_text="Ending City")
    via = forms.CharField(max_length=128, help_text="Via")
    date = forms.DateField(help_text="date in dd/mm/yy")
    rslug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Route

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')
