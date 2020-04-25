from django.shortcuts import render
from .scraping import scrape

def index(request):
    return render(request, 'userinfo/index.html')


def detail(request):
    user = request.POST['user']  # user is the name of the input
    #rank,color,ar,institute,ac,wa,tle,rte,mle,challenged,cpe,skipped,ile,other = scrape(user)
    verdict = scrape(user)
    exists = verdict[0]
    if(exists == False):
        return render(request, 'userinfo/detail.html', {'exists':exists})
    else:
        rank = verdict[1]
        color = verdict[2]
        ar = verdict[3]
        institute = verdict[4]
        ac=verdict[5]
        wa=verdict[6]
        tle=verdict[7]
        rte=verdict[8]
        mle=verdict[9]
        challenged=verdict[10]
        cpe=verdict[11]
        skipped=verdict[12]
        ile=verdict[13]
        other =verdict[14]
        rating =verdict[15]
        return render(request, 'userinfo/detail.html', {'exists':exists,'user': user, 'rank':rank,'color':color,'ar':ar,'institute':institute,'ac':ac,'wa':wa,'tle':tle,'rte':rte,'mle':mle,'challenged':challenged
        ,'cpe':cpe,'skipped':skipped,'ile':ile,'other':other,'rating':rating})
        #return render(request, 'userinfo/detail.html', {'user': user, 'verdict':verdict,})


