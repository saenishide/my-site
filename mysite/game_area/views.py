from django.shortcuts import render

# Create your views here.
def display_top(request):
    return render(request, 'gametop.html')