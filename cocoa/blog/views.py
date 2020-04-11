from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# blog
def post_new(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.save()
    return redirect('post_detail', post.pk)
    # 페이지 이동
    # 잘 제출되었습니다 멘트
  else:
    # request.method == "GET"
    form = PostForm()
    
  return render(request, 'post_new.html', {'form' : form})

def post_home(request):
  posts = Post.objects.all()
  return render(request, 'post_home.html', {
    'posts' : posts })

def post_detail(request, post_pk):
  post = Post.objects.get(pk = post_pk)
  return render(request, 'post_detail.html', {
    'post' : post
  })

def post_edit(request, post_pk):
  post = Post.objects.get(pk = post_pk)
  form = PostForm(post)
  return render(request, 'post_new.html', {
    'form' : form,
  })
  
# WORD COUNT
def count(request):
  return render(request, 'count.html')

def home(request):
  return render(request, 'home.html')

def result(request):
  text = request.POST['text']
  splitted_text = text.split(' ')
  word_len = len(splitted_text)

  return render(request, 'result.html', {
    'word_len' : word_len,
    'text' : text,
  })
  # text = '코코아 짱짱맨 화이팅'
  # splitted_text = ['코코아', '짱짱맨', '화이팅']
  # len(splitted_text) = 3


