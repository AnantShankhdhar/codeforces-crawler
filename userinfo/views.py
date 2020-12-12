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
    elif verdict[1] == False:
        exists = verdict[0]
        contests_given = verdict[1]
        name = verdict[2]
        rating = verdict[3]
        maxrating = verdict[4]
        country = verdict[5]
        city = verdict[6]
        organisation = verdict[7]
        rank = verdict[8]
        maxrank = verdict[9]

        Taglist = verdict[10]
        ProbRat = verdict[11]
        TypeList = verdict[12]
        LangList = verdict[13]
        VerdictList = verdict[14]
        return  render(request, 'userinfo/detail.html',
                       {'exists': exists,
                        'contests_given': contests_given,
                        'name': name,
                        'rating':rating}
                       )
    else:
        exists = verdict[0]
        contests_given = verdict[1]
        name = verdict[2]
        rating = verdict[3]
        maxrating = verdict[4]
        country = verdict[5]
        city = verdict[6]
        organisation = verdict[7]
        rank = verdict[8]
        maxrank = verdict[9]

        Taglist = verdict[10]
        ProbRat = verdict[11]
        TypeList = verdict[12]
        LangList = verdict[13]
        VerdictList = verdict[14]

        contestTime = verdict[15]
        ranks = verdict[16]
        oldRatings = verdict[17]
        newRatings = verdict[18]
        bestRank = verdict[19]
        worstRank = verdict[20]

        ac=VerdictList['OK']

        VerdictList['Accepted'] = VerdictList['OK']
        del VerdictList['OK']


        TypeList_label = []
        TypeList_data = []

        for i in sorted (TypeList) :
            TypeList_data.append(TypeList[i])
            TypeList_label.append(i)

        LangList_label = []
        LangList_data = []

        for i in sorted (LangList) :
            LangList_data.append(LangList[i])
            LangList_label.append(i)

        VerdictList_label = []
        VerdictList_data = []

        for i in sorted (VerdictList) :
            VerdictList_data.append(VerdictList[i])
            VerdictList_label.append(i)

        return render(request, 'userinfo/detail.html',
                      {'exists': exists,
                       'contests_given': contests_given,
                       'name': name,
                       'rating': rating}
                      )

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
