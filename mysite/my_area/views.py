from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from my_area.service.postService import PostService
from my_area.form.postForm import PostForm

###############
# 表示
###############
def display_top(request):
    post_list = PostService().getAll()
    return render(request, 'top.html', {'postList': post_list})

def display_create(request):
    imgUrlChange = 'false'
    if request.method == 'GET':
        post = PostForm.newInstance()
    elif request.method == 'POST':
        form = PostForm(request.POST)
        post = form.data
        imgUrlChange = post['imgUrlChange']
    return render(request, 'edit.html', {'post': post, 'mode': 'create', 'imgUrlChange': imgUrlChange})

def display_detail(request, post_id):
    post = PostService.getById(post_id=post_id)
    return render(request, 'detail.html', {'post': post})

def display_edit(request, post_id):
    imgUrlChange = 'false'
    if request.method == 'GET':
        post = PostService.getById(post_id)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        post = form.data
        imgUrlChange = post['imgUrlChange']
    return render(request, 'edit.html', {'post': post, 'mode': 'edit', 'imgUrlChange': imgUrlChange})

###############
# 確認
###############
def confirm_delete(request, post_id):
    post = PostService.getById(post_id=post_id)
    return render(request, 'confirm.html', {
        'post': {
            'id': post_id,
            'title': post.title,
            'todayWord': post.todayWord,
            'imgUrl': post.imgUrl,
        },
        'mode': 'delete'
    })

def confirm_edit(request, post_id):
    post = PostService.getById(post_id)
    form = PostForm(request.POST, instance=post)
    return render(request, 'confirm.html', {
        'post': {
            'id': post_id,
            'title': form.data['title'],
            'todayWord': form.data['todayWord'],
            'imgUrl': form.data['imgUrl'],
            'imgUrlChange': form.data['imgUrlChange'],
        }
        , 'mode': 'edit'
    })

def confirm_create(request):
    form = PostForm(request.POST, instance=PostForm.newInstance())
    return render(request, 'confirm.html', {
        'post': {
            'id': '',
            'title': form.data['title'],
            'todayWord': form.data['todayWord'],
            'imgUrl': form.data['imgUrl'],
            'imgUrlChange': form.data['imgUrlChange'],
        }
        , 'mode': 'create'
    })

###############
# 実行
###############
def create_post(request):
    form = PostForm(request.POST, instance=PostForm.newInstance())
    if form.is_valid():
        if form.data['imgUrlChange'] == 'true':
            PostService.moveImage(request.POST['imgUrl'])
        post = form.save(commit=False)
        post.save()
        return render(request, 'complete.html', {'post': post, 'mode': 'create'})
    return render(request, 'edit.html', {'post': post, 'mode': 'create'})

def edit_post(request, post_id):
    post = PostService.getById(post_id)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        if form.data['imgUrlChange'] == 'true':
            PostService.moveImage(request.POST['imgUrl'])
        post = form.save(commit=False)
        post.save()
        return render(request, 'complete.html', {'post': post, 'mode': 'edit'})
    return render(request, 'edit.html', {'post': form.data, 'mode': 'edit'})

def delete_post(request, post_id):
    post = PostService.getById(post_id)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.deleteFlag = True
        post.save()
        return render(request, 'complete.html', {'post': post, 'mode': 'delete'})
    return render(request, 'confirm.html', {'post': post, 'mode': 'delete'})

@csrf_exempt
def imgupload(request):
    image = request.FILES.get('image')
    if image:
        extension = image.name.split('.')[-1]
        image.name = PostService.getHashName(image.name, extension)
        PostService.uploadImage(image)
        return JsonResponse({"file_name": image.name})
    return JsonResponse({"error": "No image uploaded"}, status=400)
