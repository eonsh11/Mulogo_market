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
    if request.method =='GET':
        # 로그인한 사용자인 것을 알려주다.
        user = request.user.is_authenticated
        # 만약 로그인한 사용자가 맞다면 home화면으로 넘어갈 것이다.
        if user:
            # TweetModel에 저장한 모든 데이터들을 만들어진 순서(최신순)대로 정렬해서 불러오겠다.
            all_post = PostModel.objects.all().order_by('-created_at')
            return render(request, 'post/home.html', {'post': all_post})
        # 로그인한 사용자가 아니라면 다시 로그인화면으로 갈 것이다.
        else:
            return redirect('/sign-in')


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



