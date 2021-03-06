from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone
# from .forms import BlogForm

def home(request):
    return render(request, 'blogapp/blog.html')

#블로그 글 작성 HTMl을 보여주는 함수
def new(request):
    return render(request, 'blogapp/new.html')

#블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

#django form을 이용해서 입력값을 받는 함수
#GET 요청과 (= 입력값을 받을 수 있는 Html을 갖다 줘야함)
#POST 요청 (= 입력한 내용을 데이터 베이스에 저장. form에서 입력한 내용을 처리)
#둘 다 처리가 가능한 함수
# def formcreate(request):
#     if (request.method == 'POST'):
#         #입력 내용을 DB에 저장
#     else:
#         #입력을 받을 수 있는 Html을 갖다 주기
#         form = BlogForm()
#     return render(request, 'blogapp/form_create.html', {'form':form} )