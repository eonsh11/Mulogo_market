from django.http import request
from django.shortcuts import render, redirect
from .models import PostModel
from django.contrib.auth.decorators import login_required



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


@login_required
def delete_post(request, id):
    # 게시된 게시물들중에서 아이디가 로그인된 아이디를 가져온다.
    my_post = PostModel.objects.get(id=id)
    # 게시물을 삭제함
    my_post.delete()
    # 트윗url로 redirect시켜준다.
    return redirect('/main')


@login_required
# 각 게시물에 들어갈 수 있는 기능
def detail_post(request, id):
    # 게시된 게시물의 아이디가 같은 것을 불러온다.
    my_post = PostModel.objects.get(id=id)
    # 게시물에 저장된 댓글들을 불러와야 한다. 불러 올때는 filter 메소드를 활용하여 댓글이 생성된 순으로 정렬하여 보여준다.
    # tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
    # 렌더링을 통해 아래 url로 이동한다. 해당 url로 이동할 때에 게시글과 댓글들을 함께 보내준다.
    return render(request,'post/post_detail.html',{'post':my_post})