#Django imports
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#Forms imports
from .forms import SignupForm, ProfileForm
#Decorator import
from .decorator import auth_user_restriction


@auth_user_restriction
def signup_view(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='user/signup.html',
        context={'form': form}
    )

@auth_user_restriction
def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request,user)
            return redirect('posts:feed')
        else:
            return render (request,'user/login.html', {'error': 'invalid user of password'})

    return render (request,'user/login.html')


@login_required
def logout_view(request):
    logout(request)
    
    return redirect('users:login')


@login_required
def update_profile(request):

        profile = request.user.profile

        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data

                profile.website = data['website']
                profile.phone_number = data['phone_number']
                profile.biographi = data['biographi']
                profile.picture = data['picture']
                profile.save()

                return redirect('users:update_profile')

        else:
            form = ProfileForm()
        
        return render(
            request=request, 
            template_name='user/update_profile.html',
            context={
                'profile': profile,
                'user': request.user
            }
        )