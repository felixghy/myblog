"""blog_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

app_name = 'blog_app1'
urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    # path('post_list',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('createpost/',views.CreatePostView.as_view(),name='post_create'),
    path('updatepost/<int:pk>',views.UpdatePostView.as_view(),name='post_update'),
    path('deletepost/<int:pk>',views.DeletePostView.as_view(),name='post_delete'),
    path('draftpost/',views.DraftPostView.as_view(),name='post_draft'),
    path('comment/<int:pk>',views.add_comment_to_post,name='add_comment_to_post'),
    path('approvecomment/<int:pk>',views.comment_approve,name='comment_approve'),
    path('delcomment/<int:pk>',views.comment_delete,name='comment_delete'),
    path('pubPost/<int:pk>',views.post_publish,name='post_publish'),

    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout',LogoutView.as_view(), name='logout',kwargs={'next_page':'/'}),


]
