from django.http import request
from django.shortcuts import render, redirect
from .models import PostModel


def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/main')
    else:
        return redirect('/sign-in')


def main(request):
    return render(request, 'post/home.html')


def create_post(request):
    if request.method == "GET":
        return render(request, 'post/create-post.html')
    elif request.method == "POST":
        user = request.user
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        photo = request.POST.get('url', '')
        if content == '':
            return render(request, 'post/create-post.html', {'error': '게시글은 공백일 수 없습니다'})
        my_tweet = PostModel.objects.create(
            user=user, title=title, photo=photo, content=content)
        my_tweet.save()
        return redirect('/main')
