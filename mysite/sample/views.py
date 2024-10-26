from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from sample.models import Post # Modelで定義した関数

# View = 処理の定義
# Create your views here.

# 新たなデータを作成する
def create_post(request):
    post = Post()

    # ページロード
    if request.method == 'GET':
        # form を生成
        form = PostForm(instance=post) # 新しいpostでフォームを作成

        return render(request, 
                      'sample/post_form.html', # 呼び出すhtml
                      {'form': form}           # htmlに渡すデータ
                      )
    
    # データ送信時
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        # バリデートOKの場合
        if form.is_valid():
            # データを作成
            post = form.save(commit=False) # commit=Falseで保存を保留
            post.save()# 本当はこの前に何かデータの加工をする場合があるので、commit=Falseで保存を保留している

        return redirect('sample:read_post')

# データ一覧を表示する
def read_post(request):
    # 一覧取得
    posts = Post.objects.all().order_by('id')
    return render(request,
                  'sample/post_list.html',
                  {'posts': posts})

# 対象データを編集する
def edit_post(request, post_id):
    # pkでデータ取得
    post = get_object_or_404(Post, pk=post_id)

    # ページロード
    if request.method == 'GET':
        form = PostForm(instance=post)

        return render(request,
                      'sample/post_form.html',
                      {'form': form, 'post_id': post_id}
                      )

    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        # 入力されたデータのバリデート
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        
        # 一覧画面にリダイレクト
        return redirect('sample:read_post')

# 対象データを削除する
def delete_post(request, post_id):
    # pkでデータ取得
    post = get_object_or_404(Post, pk=post_id)
    post.delete()

    return redirect('sample:read_post')

# フォーム定義
class PostForm(ModelForm): # ModelFormを継承することで、Modelのデータをフォームに変換できる
    class Meta: # 基本の書き方。Metaクラスを継承することで、どのModelを使うかを指定できる
        model = Post
        fields = ('name', 'micropost')