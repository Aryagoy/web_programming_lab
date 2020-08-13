from django import forms


from .models import loginform



class login_form(forms.ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Enter Your Name"}))
    reg_no = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Enter your Reg number"}))
    dept = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Enter your department"}))
    degree = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Enter your degree"}))
    class Meta:
        model = loginform
        fields = ['name','reg_no','dept','degree']
