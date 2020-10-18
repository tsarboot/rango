from django import forms
from django.contrib.auth.models import User
from rango.models import Category,Car,UserProfil
def retreiveData():
    cursor = sqlite3.connect('../db.sqlite3').cursor()
    cursor.execute('')

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text='enter the category name')
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta :
        model = Category
        fields = ('name',)
class CarForm(forms.ModelForm):
   
    category = forms.ChoiceField(choices=[], required=False)
    title = forms.CharField(max_length=128,help_text='enter the car name')
    url = forms.URLField(max_length=128,help_text='enter the car url')
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    class Meta:
        model = Car
        exclude = ()
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),min_length=2)
    class Meta :
        model = User 
        fields = ('username','email','password')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfil
        fields = ('website','picture')
