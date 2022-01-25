from django.http import request
from django.shortcuts import render, redirect
from .models import PostModel
from .models import PostComment
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


@login_required
# 댓글을 쓰는 기능(인자로 id를 넘겨준다.)
def write_comment(request, id):
    # 만약 데이터전송 방식이 POST라면
    if request.method == 'POST':
        # 댓글을 저장한다.
        comment = request.POST.get("comment","")
        # 작성자가 작성한 댓글을 모두 불러온다.
        current_post = PostModel.objects.get(id=id)
        # 모델을 임포트해와서 TweetComment클래스를 이요하여 객체를 생성한다.
        PS = PostComment()
        # 댓글정보
        PS.comment = comment
        # 작성자 정보
        PS.user = request.user
        # 댓글을 작성하는 게시글 정보
        PS.post = current_post
        # 저장한다. save()메소드
        PS.save()
        # redirect를 이용하여 tweet/ 지금 작성하고있는 게시글을 붙여준다. 타입 str로 변환
        return redirect('/main/'+str(id))


@login_required
# 댓글을 삭제하는 기능 
# 내가 작성한 댓글들임을 알아야 하기 때문에 id를 인자로 받는다.
def delete_comment(request, id):
    # 나의 id로 작성한 댓글을 변수에 할당
    comment = PostComment.objects.get(id=id)
    # 내가 작성한 댓글의 게시물의 id를 변수에 할당
    current_post = comment.post.id
    # 해당 댓글을 삭제하는 delete()메소드 활용
    comment.delete()
    # 다시 해당 게시물의 url주소로 이동
    return redirect('/main/'+str(current_post))