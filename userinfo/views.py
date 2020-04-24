from django.shortcuts import render
from .scraping import scrape

def index(request):
    return render(request, 'userinfo/index.html')


def detail(request):
    user = request.POST['user']  # user is the name of the input
    #rank,color,ar,institute,ac,wa,tle,rte,mle,challenged,cpe,skipped,ile,other = scrape(user)
    verdict = scrape(user)
    rank = verdict[0]
    color = verdict[1]
    ar = verdict[2]
    institute = verdict[3]
    #rating = verdict[4]
    ac=verdict[4]
    wa=verdict[5]
    tle=verdict[6]
    rte=verdict[7]
    mle=verdict[8]
    challenged=verdict[9]
    cpe=verdict[10]
    skipped=verdict[11]
    ile=verdict[12]
    other =verdict[13] 
    rating =verdict[14]
    return render(request, 'userinfo/detail.html', {'user': user, 'rank':rank,'color':color,'ar':ar,'institute':institute,'ac':ac,'wa':wa,'tle':tle,'rte':rte,'mle':mle,'challenged':challenged
    ,'cpe':cpe,'skipped':skipped,'ile':ile,'other':other,'rating':rating})
    #return render(request, 'userinfo/detail.html', {'user': user, 'verdict':verdict,})


