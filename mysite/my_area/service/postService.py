from my_area.models import Post
from django.db import models
from django.conf import settings

class PostService:

    """
    取得
    """
    def getAll(self):
        return Post.objects.filter(deleteFlag=False).order_by('id')

    def getById(post_id):
        return Post.objects.filter(id=post_id, deleteFlag=False).first()
    
    """
    操作
    """
    def uploadImage(image):
        url = settings.STATICFILES_DIRS[0] + '/img/temp/' + image.name
        file = models.FileField(upload_to=url)
        return file