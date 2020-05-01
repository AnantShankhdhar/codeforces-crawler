from django.shortcuts import render,redirect
from .scraping import scrape
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'userinfo/index.html')


    


def detail(request):
    user = request.POST['user']  # user is the name of the input
    # rank,color,ar,institute,ac,wa,tle,rte,mle,challenged,cpe,skipped,ile,other = scrape(user)
    verdict = scrape(user)
    if verdict == False:
        exists = verdict
        return render(request, 'userinfo/detail.html', {'exists': exists})
    else:
        exists = verdict[0]
        rank = verdict[1]
        color = verdict[2]
        ar = verdict[3]
        institute = verdict[4]
        ac = verdict[5]
        wa = verdict[6]
        tle = verdict[7]
        rte = verdict[8]
        mle = verdict[9]
        challenged = verdict[10]
        cpe = verdict[11]
        skipped = verdict[12]
        ile = verdict[13]
        other = verdict[14]
        rating = verdict[15]
        Taglist = verdict[16]
        RatingList = verdict[17]
        TypeList = verdict[18]
        LangList = verdict[19]
        
        return render(request, 'userinfo/detail.html',
                      {'exists': exists, 'user': user, 'rank': rank, 'color': color, 'ar': ar, 'institute': institute,
                       'ac': ac, 'wa': wa, 'tle': tle, 'rte': rte, 'mle': mle, 'challenged': challenged
                          , 'cpe': cpe, 'skipped': skipped, 'ile': ile, 'other': other, 'rating': rating,})
        # return render(request, 'userinfo/detail.html', {'user': user, 'verdict':verdict,})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name=form.cleaned_data.get('first_name')
            user.profile.sur_name=form.cleaned_data.get('sur_name')
            user.profile.email=form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username,password=raw_password)
            return redirect('userinfo:index')
    else:
        form = SignUpForm()
    return render(request, 'userinfo/signup.html', {'form': form})