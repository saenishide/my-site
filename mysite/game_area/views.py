from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random
from django.conf import settings
from game_area.apps import GameAreaConfig
import re

# Create your views here.
def display_top(request):
    return render(request, 'gametop.html')

@csrf_exempt
def select_zero_or_one(request):
    result = 0
    if request.method == 'POST':
        random_data = str(random.randint(0, 1)) # 0 or 1
        # requestからPOSTで送られてきた値を取得
        data = request.POST['select']
        if random_data == data:
            result = 1
        else:
            result = -1
    
    return JsonResponse({"result": result})

@csrf_exempt
def check_number(request):
    if request.method == 'POST':
        number_img = request.FILES.get('image')
        file_path = settings.STATICFILES_DIRS[1] + '/img/' + 'test.jpg'
        with open(file_path, 'wb+') as destination:
            for chunk in number_img.chunks():
                destination.write(chunk)
        result = GameAreaConfig.mservice.check_number(number_img)

        return JsonResponse({"result": result})

@csrf_exempt
def sort_get_list(request):
    num = request.POST.get('number')
    data = [25,3,49,67,14,5,9,10,2,1]
    data.sort(reverse=True)
    return JsonResponse({"result": data[:int(num)]})

@csrf_exempt
def check_string(request):
    if request.method == 'POST':
        str_data = request.POST.get('text')

        # 郵便番号の正規表現
        ptn = re.compile(r'^(\d{3})-(\d{4})$')
        # 郵便番号を抽出
        if result := ptn.search(str_data):
            return JsonResponse({"result": "郵便番号上3桁は" + result.group(1) + "、下4桁は" + result.group(2) + "です。"})
        else:
            return JsonResponse({"result": "郵便番号の形式ではありませんよほほほ。"})