from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random
from django.conf import settings
from game_area.apps import GameAreaConfig 

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

    
    