from django import forms
from .models import TeacherInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.forms import ModelForm

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class NameForm(forms.Form):
    #model = TeacherInfo
    first_name = forms.CharField(label='First name', max_length=100)


    
    #class Meta:
        #model = TeacherInfo
        #fields = ("first_name")

class TeacherForm(ModelForm):
    class Meta:
        model = TeacherInfo
        fields = ['first_name', 'last_name', 'subject', 'supply_list','supply_list', 'supply_cost',]


#class SearchResultsView(ListView):
    #model = TeacherInfo
    #template_name = 'search.html'

    #def get_queryset(self): # new
        #return TeacherInfo.objects.filter(
            #Q(name__icontains='Jaemin') | Q(state__icontains='Na')
        #)
