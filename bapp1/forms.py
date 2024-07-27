#from django import forms
from django import forms
from .models import UserRegistration

class UserRegisterForm(forms.ModelForm):
    USER_TYPES = [
        ('donor','Donor'),
        ('seeker','Seeker'),
        ('hospital','Hospital'),
        ('bloodbank','Blood Bank'),
    ]
    GENDER_TYPES = [
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
        
    ]

    BLOOD_GROUPS = [
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),

    ]
    STATES = [
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    ]

    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.Select(attrs={'class': 'form-control'}), label="User Type")
    blood_type_group = forms.ChoiceField(choices=BLOOD_GROUPS, widget=forms.Select(attrs={'class': 'form-control'}), label="Blood Type Group")
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="User Name")
    userage = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label="User Age")
    usermobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="User Mobile")
    useremail = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="User Eamil")
    usergender = forms.ChoiceField(choices=GENDER_TYPES,widget=forms.Select(attrs={'class': 'form-control'}), label="Gender")
    flat_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Flat No")
    street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Street")
    village = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Village")
    town = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Town")
    district = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="District")
    state = forms.ChoiceField(choices=STATES, widget=forms.Select(attrs={'class': 'form-control'}), label="State")
    pincode = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Pincode")
    
    def __str__(self):
        return self.username
    
   

# class BloodSearchForm(forms.Form):
#     blood_type = forms.CharField(max_length=3)

    

    class Meta:
        model = UserRegistration
        fields = '__all__'

# class UserRegisterForm(forms.ModelForm):
#      class Meta:
#          model = DonorRegister
#          fields = '__all__'