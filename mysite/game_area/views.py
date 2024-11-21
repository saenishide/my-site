from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random

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
    
    