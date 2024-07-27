from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from .models import UserRegistration
#from .forms import BloodSearchForm
#from .models import Donor

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = UserRegistration(  # Use your actual model name here
                user_type=form.cleaned_data['user_type'],
                blood_type_group=form.cleaned_data['blood_type_group'],
                username=form.cleaned_data['username'],
                userage=form.cleaned_data['userage'],
                usermobile=form.cleaned_data['usermobile'],
                useremail=form.cleaned_data['useremail'],
                usergender=form.cleaned_data['usergender'],
                flat_no=form.cleaned_data['flat_no'],
                street=form.cleaned_data['street'],
                village=form.cleaned_data['village'],
                town=form.cleaned_data['town'],
                district=form.cleaned_data['district'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode']
            )
            data.save()
            return redirect('success')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

def profile(request):
    registrations = UserRegistration.objects.all()
    context = {
        'registration': registrations,
    }
    return render(request, 'profile.html', context)

def success_view(request):
    return render(request, 'success.html')


def update_view(request):
    return render(request, 'update.html')

def Donor_profile_view(request):
    registrations = UserRegistration.objects.filter(user_type='donor')
    context = {
        'registration': registrations,
    }
    return render(request, 'Donor_profile.html', context)


def Seeker_profile_view(request):
    registrations = UserRegistration.objects.filter(user_type='seeker')
    context = {
        'registration': registrations,
    }
    return render(request, 'seeker_profile.html', context)


def dashboard_view(request):
    return render(request, 'dashboard.html')


def edit_profile(request, id):
    profile = get_object_or_404(UserRegistration, pk=id)

    if request.method == 'POST':
        form = UserRegisterForm(request.POST, instance=profile)
        
        if form.is_valid():
            print('\n\nDonor regn form is valid\n\n')
            form.save()
            return redirect('update')
        else:
            print('\n\nDonor regn form is not valid\n\n')
            print(form.errors)  # Print form errors for debugging
    else:
        form = UserRegisterForm(instance=profile)

    return render(request, 'register.html', {'form': form})


def update_profile(request, pk):
      #from .models import Donor  # Local import to avoid circular import
     profile = get_object_or_404(UserRegistration, pk=pk)
     if request.method == 'POST':
          form = UserRegisterForm(request.POST, instance=profile)
          if form.is_valid():
              form.save()
              return redirect('profile_detail', pk=pk)
     else:
        form = UserRegisterForm(instance=profile)
     return render(request, 'profile/update_profile.html', {'form': form})


def delete_profile(request, id):
    profile = get_object_or_404(UserRegistration, id=id)
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Profile deleted successfully!')
        return redirect('profile')
    return render(request, 'profile/confirm_delete.html', {'profile': profile})


#def add_donation(request, donor_id):
#     donor = get_object_or_404(Donor, id=donor_id)
#     donor.increment_donations()
#     return redirect('donor_profile', donor_id=donor.id)

# def search_blood(request):
#      form = BloodSearchForm()
#      results = []
#      if request.method == 'GET':
#          form = BloodSearchForm(request.GET)
#          if form.is_valid():
#              blood_type = form.cleaned_data['blood_type']
#              results = Donor.objects.filter(blood_type=blood_type)
#      return render(request, 'search.html', {'form': form, 'results': results})

# def search_blood(request):
#      query = request.GET.get('blood_type', '')
#      results = Donor.objects.filter(blood_type__icontains=query) if query else []
#      return render(request, 'search_results.html', {'results': results, 'query': query})
