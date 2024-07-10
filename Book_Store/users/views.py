from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm



def home(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')
    
def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'register.html', {'form': form})

