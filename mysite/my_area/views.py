from django.shortcuts import render, get_object_or_404
from my_area.service.postService import PostService
from my_area.form.postForm import PostForm

"""
表示
"""
# topページを表示
def display_top(request):
    postList = PostService().getAll()
    return render(request, 'top.html', {'postList': postList})

# 新規作成ページを表示
def display_create(request):
    # form を生成
    post = PostForm.newInstance()
    form = PostForm(instance=post)
    return render(request, 'create.html', {'form': form})

# 詳細ページを表示
def display_detail(request, post_id):
    post = PostService.getById(post_id=post_id)
    return render(request, 'detail.html', {'post': post})

# 編集ページを表示
def display_edit(request, post_id):
    post = PostService.getById(post_id)
    return render(request, 'edit.html', {'post': post})

"""
確認表示
"""
# 削除確認ページを表示
def confirm_delete(request, post_id):
    post = PostService.getById(post_id=post_id)
    return render(request, 'confirm_delete.html'
                  , {'post': {
                      'id': post_id,
                      'title': post.title, 
                      'todayWord': post.todayWord,
                      'imgUrl': post.imgUrl,
                    }})

# 編集確認ページを表示
def confirm_edit(request, post_id):
    post = PostService.getById(post_id)
    image = request.FILES.get('imgUrl')
    # ファイルをアップロード
    if image is not None:
        extension = image.name.split('.')[-1]
        image.name = PostService.getHashName(image.name, extension)
        PostService.uploadImage(image)
    form = PostForm(request.POST, instance=post)
    return render(request, 'confirm_edit.html'
                  , {'post': {
                      'id': post_id,
                      'title': form.data['title'], 
                      'todayWord': form.data['todayWord'],
                      'imgUrl': image.name,
                    }})

# 新規作成確認ページを表示
def confirm_create(request):
    post = PostForm.newInstance()
    form = PostForm(request.POST, instance=post)
    return render(request
                  , 'confirm_create.html'
                  , {'post': {
                      'title': form.data['title'], 
                      'todayWord': form.data['todayWord'],
                      'imgUrl': form.data['imgUrl'],
                    }})


"""
操作
"""
# 新規作成
def create_post(request):
    post = PostForm.newInstance()
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
    return render(request, 'comp_add.html', {'post': post})

# 編集
def edit_post(request, post_id):
    # pkでデータ取得
    post = PostService.getById(post_id)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        PostService.moveImage(request.POST['imgUrl'])
        post = form.save(commit=False)
        post.save()

    return render(request, 'comp_edit.html', {'post': post})

# 削除
def delete_post(request, post_id):
    post = PostService.getById(post_id)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.deleteFlag = True
        post.save()

    return render(request, 'comp_delete.html', {'post': post})