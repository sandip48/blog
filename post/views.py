from django.shortcuts import render,redirect
from django.urls import reverse
from post.models import Post
from post.forms import PostForm
from django.conf import Settings
from django.views import View
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class PostListView(LoginRequiredMixin,View):
    def get(self,request, *args , **kwargs):
        posts = Post.objects.filter(user=request.user)
        paginator = Paginator(posts,8)
        page = request.GET.get("page",1)
        page_obj = paginator.get_page(page)
        return render(request,"post/list.html", context={"posts": page_obj})

class IndexView(View):
     def get(self,request, *args , **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts,8)
        page = request.GET.get("page",1)
        page_obj = paginator.get_page(page)
        return render(request,"index.html", context={"posts": page_obj})

class PostDetailView(View):
    def get(self, request,id,*args,**kwargs):
        post = Post.objects.get(id=id)
        return render(request,"post/detail",context={'post':post})
    
    
class PostEditView(LoginRequiredMixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            post = Post.objects.get(id=id)
            if post.user!=request.user:
                return redirect(reverse("403_error"))
            form = PostForm(instance=post)
            return render(request,"post/edit.html",context={'form':form})
        except Post.DoesNotExist:
            return redirect(reverse("404_Error"))
        except Exception:
            return redirect(reverse("500_Error"))


    def post(self,request,*args,**kwargs):
        post = Post.objects.get(id=id)
        form = PostForm(instance=post,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("post-list"))
        return render(request,"post/edit.html",context={"form":form})
    
class PostCreateView(LoginRequiredMixin,View):#only 403
    def get(self,request,*args,**kwargs):
        form = PostForm()
        return render(request,"post/create.html",context={'form':form})
    def post(self,request,*args,**kwargs):
        print("POST DATA:",request.POST,request.FILES)
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse('post-list'))
        return render (request,"post/create.html",context={'form':form})
    
class PostDeleteView(LoginRequiredMixin,View):
    def post(self,request,*args,**kwargs):
        post = Post.objects.get(id=request.POST.get("id"))
        if post.user!=request.user:
            return redirect(reverse("404_error"))
        post.delete()
        return redirect(reverse('post-list'))
        


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,8)
    page = request.GET.get('page',1)
    page_obj = paginator.get_page(page)
    return render(request,"post/list.html", context={"posts": page_obj})

def post_create(request):
    if request.method == "GET":
        form = PostForm()
        return render(request,"post/create.html",context={'form':form})
    else:
        print("POST DATA:",request.POST,request.FILES)
        form = PostForm(request.POST, request.FILES)
        # with open(f"{settings.BASE_DIR}/media/{request.FILES['image'].name}",'wb+') as media:
        #     for chunk in request.FILES['image'].chunks():
        #         media.write(chunk)
        if form.is_valid():
            # Post.objects.create(title = form.cleaned_data.get("title"),
            #                 content = form.cleaned_data.get('content'),
            #                 image=form.cleaned_data.get('image'))
            form.save()
            return redirect(reverse('post-list'))
        return render (request,"post/create.html",context={'form':form})
    
def post_edit(request,id):
    post = Post.objects.get(id=id)
    if request.method == "GET":
        return render(request,"post/edit.html",context={'post':post})
    else:
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect(reverse('post-list'))
    
def post_delete(request):
    if request.method == "POST":
        post = Post.objects.get(id=request.POST.get("id"))
        post.delete()
        return redirect(reverse('post-list'))
    
def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,"post/detail.html",context={"post":post})
