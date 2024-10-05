from django.shortcuts import render, get_object_or_404, redirect

from post.models import Post, Comment


# 게시글 목록 페이지
def index(request):
    post_list = Post.objects.all().order_by('-post_id')
    context = {'posts': post_list}
    return render(request, 'post/index.html', context)


# 게시글 상세 페이지
def detail(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    comment_list = Comment.objects.filter(post=post).order_by('-comment_id')
    context = {'post': post, 'comments': comment_list}
    return render(request, 'post/detail.html', context)


# 게시글 등록 페이지
def create_post(request):
    if not request.user.is_authenticated:
        return redirect('login:index')
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        post = Post(title=title, user=request.user, content=content)
        post.save()
        return redirect('post:detail', post_id=post.post_id)
    return render(request, 'post/create.html')


# 게시글 삭제
def delete_post(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login:index')
    if request.method == "GET":
        post = get_object_or_404(Post, post_id= post_id)
        if post.user.username != request.user.username:
            return redirect('post:detail', post_id=post.post_id)
        else:
            post.delete()
            return redirect('post:index')

# 게시글 수정
def update_post(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login:index')
    post = get_object_or_404(Post, post_id=post_id)
    if post.user.username != request.user.username:
        return redirect('post:detail', post_id=post.post_id)
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect("post:detail", post_id=post_id)
    context = {'post': post}
    return render(request, 'post/update.html', context)

# 댓글 추가
def create_comment(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login:index')
    post = get_object_or_404(Post,post_id=post_id)
    if request.method == 'POST':
        comment_content = request.POST.get('comment')
        comment_user = request.user
        comment = Comment(comment_content = comment_content, comment_user = comment_user, post=post)
        comment.save()
        return redirect('post:detail', post_id = post_id)

