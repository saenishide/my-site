import hashlib
from my_area.models import Post
from django.conf import settings
import shutil
import datetime

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
    def getHashName(imageName, extension):
        targetName = (imageName + str(datetime.datetime.now())).encode('utf-8')
        return hashlib.md5(targetName).hexdigest() + '.' + extension

    def uploadImage(image):
        file_path = settings.STATICFILES_DIRS[0] + '/img/temp/' + image.name
        with open(file_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)
    
    def moveImage(image_name):
        temp_file_path = settings.STATICFILES_DIRS[0] + '/img/temp/' + image_name
        file_dir = settings.STATICFILES_DIRS[0] + '/img/'
        shutil.move(temp_file_path, file_dir)
        