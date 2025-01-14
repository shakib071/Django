from django.shortcuts import render, redirect
from . import forms

def add_profile(request):
    profile_form = forms.ProfileForm()  # Initialize form outside of POST check
    if request.method == 'POST':
        profile_form = forms.ProfileForm(request.POST)
        if profile_form.is_valid():  # Correctly call is_valid() with parentheses
            profile_form.save()
            return redirect('add_profile')
    
    return render(request, 'add_profile.html', {'form': profile_form})
