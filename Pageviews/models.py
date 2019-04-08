from django.db import models
from .utils import get_client_ip
# Create your models here.
from django.shortcuts import get_object_or_404
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .signals import object_viewed_signal
from django.contrib.auth import get_user_model
from posts.models import Post
User = get_user_model()

class ObjectViewed(models.Model):
    user            = models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL)
    content_type    = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    object_id       = models.PositiveIntegerField()
    ip_address      = models.CharField(max_length=120, blank=True, null=True)
    content_object  = GenericForeignKey('content_type', 'object_id')
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self, ):
        return "%s viewed: %s" %(self.content_object, self.timestamp)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object Viewed'
        verbose_name_plural = 'Objects Viewed'


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)
    ip_address = None
    try:
        ip_address = get_client_ip(request)
    except:
        pass

    user = request.user
    if user.is_authenticated:
        log_in = user
    else:
        log_in = None
    new_view_instance = ObjectViewed.objects.create(
                user=log_in, 
                content_type=c_type,
                object_id=instance.id,
                ip_address=ip_address
                )
    posts = get_object_or_404(Post,id=instance.id)
    posts.comment_count = posts.comment_count + 1
    posts.save()

    # posts = Post.objects.update(comment_count=comment)

object_viewed_signal.connect(object_viewed_receiver)