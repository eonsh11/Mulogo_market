from django.http import request
from django.shortcuts import render, redirect


def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/main')
    else:
        return redirect('/sign-in')


def main(request):
    return render(request, 'post/home.html')
