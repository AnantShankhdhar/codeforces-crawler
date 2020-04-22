from django.shortcuts import render

def index(request):
    return render(request, 'userinfo/index.html' )

def detail(request):
    return render(request, 'userinfo/detail.html')
