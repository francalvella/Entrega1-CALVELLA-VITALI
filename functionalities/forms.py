from django import forms

class coins_post_form(forms.Form):
    name = forms.CharField(max_length=15)
    value = forms.FloatField()
    
    
    
class user_post_form(forms.Form):
    name = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    user_name = forms.CharField(max_length=20)
    email = forms.EmailField() 
    
    
    
class experience_post_form(forms.Form):
    user = forms.CharField(max_length=20)
    ocupation = forms.CharField(max_length=10)
    experience = forms.CharField(max_length=150)



class coin_search_form(forms.Form):
    name = forms.CharField(max_length=20)