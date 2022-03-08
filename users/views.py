from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.




def register(request):
    form = UserRegisterForm()
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!!!')
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
     
        
    context = {
        'form': form
    }
    
    return render(request, 'users/register.html', context)


def profile(request):
    return render(request, 'users/profile.html')