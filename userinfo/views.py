from django.shortcuts import render
from .scraping import scrape

def index(request):
    return render(request, 'userinfo/index.html')


def detail(request):
    user = request.POST['user']  # user is the name of the input
    verdict = scrape(user)
    rank = verdict[0]
    color = verdict[1]
    ar = verdict[2]
    institute = verdict[3]
    return render(request, 'userinfo/detail.html', {'user': user, 'rank':rank,'color':color,'ar':ar,'institute':institute,})



