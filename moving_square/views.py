

from django.shortcuts import render, redirect


def home(request):
    # Return a simple page or render your game here
    return render(request, 'home.html')  #moving_square/home.html


