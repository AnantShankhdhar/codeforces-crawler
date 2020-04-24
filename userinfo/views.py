from django.shortcuts import render
<<<<<<< HEAD
from .scraping import scrape
=======

>>>>>>> 0a6fbabf87ea76d2364de2f9cf5041a9aeae9cbd

def index(request):
    return render(request, 'userinfo/index.html')


def detail(request):
    user = request.POST['user']  # user is the name of the input
<<<<<<< HEAD
    verdict = scrape(user)
    rank = verdict[0]
    color = verdict[1]
    ar = verdict[2]
    institute = verdict[3]
    return render(request, 'userinfo/detail.html', {'user': user, 'rank':rank,'color':color,'ar':ar,'institute':institute,})

=======
    return render(request, 'userinfo/detail.html', {'user': user, })
>>>>>>> 0a6fbabf87ea76d2364de2f9cf5041a9aeae9cbd


