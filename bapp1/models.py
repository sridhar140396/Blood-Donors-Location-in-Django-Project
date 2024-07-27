from django.db import models
from django import forms

# Create your models here.
class UserRegistration(models.Model):
    USER_TYPES = [
        ('donor','Donor'),
        ('seeker','Seeker'),
        ('hospital','Hospital'),
        ('bloodbank','Blood Bank'),
    ]
    GENDER_TYPES = [
        ('male','MALE'),
        ('female','FEMALE'),
        ('others','OTHERS'),
        
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

    user_type = models.CharField(choices=USER_TYPES, max_length=100)
    blood_type_group = models.CharField(choices=BLOOD_GROUPS, max_length=100)
    username = models.CharField(max_length=50)
    userage = models.IntegerField(max_length=50)
    usermobile = models.CharField(max_length=15)
    useremail = models.EmailField(max_length=100)
    usergender = models.CharField(choices=GENDER_TYPES, max_length=100)
    flat_no = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(choices=STATES, max_length=100)
    pincode = models.IntegerField(max_length=100)

    def __str__(self):
        return self.username
    
# class Donor(models.Model):
#     # Other fields...
#     total_donations = models.PositiveIntegerField(default=0)

#     def increment_donations(self):
#         self.total_donations += 1
#         self.save()




# class UserRegister(models.Model):
#      name = models.CharField(max_length=100)
#      blood_type = models.CharField(max_length=3)
    
# class UserRegisterForm(forms.ModelForm):

#     class Meta:
#          model = DonorRegister
#          fields = '__all__'