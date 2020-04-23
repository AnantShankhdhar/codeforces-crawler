from django.shortcuts import render


def index(request):
    return render(request, 'userinfo/index.html')


def detail(request):
    user = request.POST['user']  # user is the name of the input
    return render(request, 'userinfo/detail.html', {'user': user, })


