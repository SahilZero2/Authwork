from django.shortcuts import render
from django.views.generic import CreateView , UpdateView, DeleteView
from .models import  Post
from django.urls import reverse_lazy

# Create your views here.
def blog(request):
    myposts = Post.objects.all()
    print(myposts)
    return render(request,'blogindex.html',{"myposts" : myposts})

def blogpost(request,id):
    post = Post.objects.filter(post_id = id)[0]
    print(post)
    return render(request,'blogpost.html',{'post' : post})


class AddPostView(CreateView):
    model = Post
    template_name = 'addpost.html'
    fields = 'title slug content thumbnail profile author'.split()

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'updateview.html'
    fields = 'title  content thumbnail '.split()

class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('blog')
    



