from django import forms  

from .models import Task , Category 



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name' , 'description']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'})

        }






class TaskForm(forms.ModelForm):

    class Meta:
        model=Task 
        fields = ['title' , 'description' , 'status' ,'priority' ,  'due_date' , 'category']
        # fields = 'all'

        # Dictinary for assigning style classes 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.NumberInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }



# forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
