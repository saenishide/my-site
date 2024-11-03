from my_area.models import Post

class PostService:

    """
    取得
    """
    def getAll(self):
        return Post.objects.filter(deleteFlag=False).order_by('id')

    def getById(post_id):
        return Post.objects.filter(id=post_id, deleteFlag=False).first()