from django import forms



class UserRegistration(forms.Form):

    username = forms.CharField(label="Username", max_length=10, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.EmailField(label="Email", max_length=20, min_length=10,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    password = forms.CharField(label="Password", max_length=20, min_length=8,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    renter_password = forms.CharField(label="Renter Password", max_length=20, min_length=8,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))