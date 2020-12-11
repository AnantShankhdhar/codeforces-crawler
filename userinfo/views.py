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

        rating = verdict[5]
        Taglist = verdict[6]
        RatingList = verdict[7]
        TypeList = verdict[8]
        LangList = verdict[9]
        VerdictList = verdict[10]
        ac=VerdictList['OK']

        return render(request, 'userinfo/detail.html',
                      {'exists': exists, 'user': user, 'rank': rank, 'color': color, 'ar': ar, 'institute': institute,
                        'rating': rating, 'ac':ac})

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
