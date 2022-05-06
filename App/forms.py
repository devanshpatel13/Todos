from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from django import forms
from .models import Todo




#authentication Part
class registerview(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))#
    class Meta:
        model=User
        fields=['username','first_name','email','password1','password2']
        widgest={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'})
        }

class loginview(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    class Meta:
        model=User
        fields=["username","password"]
#
class changepass(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter New Password"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Re-Enter New Password"}))

class passreset(SetPasswordForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control mb-3','placeholder':'Enter Your Registered E-Mail'}))

class setresetpass(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Enter New Password"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Re-Enter New Password"}))

#end auth




class todoform(forms.ModelForm):
    class Meta:
        model = Todo
        fields=['title','descripation','date']

