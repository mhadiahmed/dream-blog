from django.shortcuts import render,get_object_or_404,redirect
from comments.models import comment
from comments.forms import CommentForm
from .models import Post,Category,Author
from django.contrib.contenttypes.models import ContentType
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from Pageviews.signals import object_viewed_signal
from Pageviews.models import ObjectViewed
def index(request):
    queryset = Post.objects.filter(featured=False)
    context = {
        'object_list': queryset
    }
    return render(request, 'index.html', context)

    

def blog(request):
    return render(request, 'article.html', {})


def list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    posts = Post.objects.all().filter(featured=False)
    Popular = Post.objects.filter(featured=False).order_by('-comment_count')[:5]
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        posts = posts.filter(categories=category)
        latest = Post.objects.filter(featured=False,categories=category).order_by('-timestamp')[0:3]
        last = Post.objects.filter(featured=False).last()
        context = {
        'posts':posts,
        'categories':categories,
        'latest':latest,
        'category':category,
        'last':last,
        'Popular':Popular,
        }
        return render(request,'categorys.html',context)

    lats_one = Post.objects.filter(featured=False).last()
    # before_last = Post.objects.all().last()
    context = {
        'posts':posts,
        'lats_one':lats_one,
        'categories':categories,
        'Popular':Popular
    }
    return render(request,'list.html',context)


def detail(request,id):
    lats_one = Post.objects.all().last()
    # before_last = Post.objects.all().last()
    posts = Post.objects.all().filter(featured=False)
    post = get_object_or_404(Post,id=id)
    hit_count = HitCount.objects.get_for_object(post)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    comments = comment.objects.filter_by_instance(post)
    object_viewed_signal.send(post.__class__,instance=post,request=request)
    initial_data = {
        "content_type": post.get_content_type,
        "object_id": post.id
    } 
    _form = CommentForm(request.POST or None, initial=initial_data)
    if _form.is_valid() and request.user.is_authenticated:
        c_type = _form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = _form.cleaned_data.get("object_id")
        content_data = _form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()
                
        new_comment = comment.objects.get_or_create(
                        user = request.user,
                        content_type = content_type,
                        object_id = obj_id,
                        content = content_data,
                        parent = parent_obj,
                        
            )
        return redirect(post.get_absolute_url())
    context = {
        'post':post,
        'posts':posts,
        'lats_one':lats_one,
        "comments":comments,
        "coments_form":_form,
    }
    return render(request,'detail.html',context)


# def about(request):
#     context = {
#     'about':'About'
#     }
#     return render(request,'About.html',context)





#     posts = Post.objects.all()
# class Blog(models.Model):
#     #fields you need
#     blog_views=models.IntegerField(default=0)
# views.py

# def blog_post(request,post_id):
#     #your code
#     blog_object=Blog.objects.get(id=post_id)
#     blog_object.blog_views=blog_object.blog_views+1
#     blog_object.save()
#     #your code


