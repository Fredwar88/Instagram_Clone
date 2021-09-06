# django Libs
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# forms
from .forms import PostForm
# models
from .models import Post


@login_required
def posts_list(request):

    posts = Post.objects.all().order_by('-created')

    return render(request,'post/feed.html', {'posts' : posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post:feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='post/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )