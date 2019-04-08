from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    slug = models.SlugField(max_length=200,db_index=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    featured = models.BooleanField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post:detail-page", kwargs={"id":self.id})

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

# class Subscribe(models.Model):
#     email = models.EmailField()
#     class Meta:
#         verbose_name = "Subscribe"
#         verbose_name_plural = "Subscribes"

#     def __str__(self):
#         return self.email
#     