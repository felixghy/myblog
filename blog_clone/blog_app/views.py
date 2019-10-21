from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
CreateView,UpdateView,DeleteView)
from .models import Post,Comment
from django.utils import timezone
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm,CommentForm
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
class IndexView(TemplateView):
    template_name ='index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    #default template post_list.html
    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
class PostDetailView(DetailView):
    """docstring for PostDetailView."""
    model = Post
    # default tamplete post_detail.html

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name ='post_details.html'
    model = Post
    #fields = ('auth','title','text')
    form_class = PostForm
    # default template post_form

class UpdatePostView(UpdateView):
    login_url = '/login/'
    redirect_field_name ='post_details.html'
    model = Post
    fields = ('title','text',)
    # default template post_update

class DeletePostView(DeleteView):
    print('------DeletePostView is called')
    model = Post
    success_url = reverse_lazy('blog_app1:post_list')

class DraftPostView(ListView):
    template_name = 'post_draft_list.html'

    model = Post
    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('create_date')

##############################
##############################
@login_required
def add_comment_to_post(request,pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #return Comment form model
            comment = form.save(commit=False)
            #link the comment to current Post.
            comment.post = post
            comment.save()

            return redirect('blog_app1:post_detail', pk=post.pk)

        else:
            print('add_comment_to_post: form is not valid')
    else:

         form = CommentForm()

    return render(request,'comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.approve()
        return redirect('blog_app1:post_detail',pk=comment.post.pk)

@login_required
def comment_delete(request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        print(f'views.comment_delete: comment is {comment} and pk is {pk}')
        post_pk = comment.post.pk
        comment.delete()
        return redirect('blog_app1:post_detail',pk=post_pk)

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)

    post.publish()
    print(f'===post publish is called ====,Post is {post},time is {timezone.now()}')
    return redirect('blog_app1:post_detail', pk=post.pk)
