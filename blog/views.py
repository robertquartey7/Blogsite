from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Post
# Create your views here.




def home(request):
    
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)



def about(request):
    context = {
        'title':'about'
    }
    return render(request, 'blog/about.html', context)

