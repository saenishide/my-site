from my_area.models import Post
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'todayWord', 'imgUrl']

    def newInstance():
        return Post()