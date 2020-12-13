from django.shortcuts import render,redirect
from .scraping import scrape
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
import datetime
import time
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

        TagList = verdict[10]
        ProbRatList = verdict[11]
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

        ProbRatList_label = []
        ProbRatList_data = []

        for i in sorted (ProbRatList) :
            ProbRatList_data.append(ProbRatList[i])
            ProbRatList_label.append(i)

        VerdictList_label = []
        VerdictList_data = []

        VerdictList = dict([(value, key) for key, value in VerdictList.items()])
        for i in sorted (VerdictList, reverse= True) :
            VerdictList_label.append(VerdictList[i])
            VerdictList_data.append(i)

        TagList_label = []
        TagList_data = []

        TagList = dict([(value, key) for key, value in TagList.items()])
        for i in sorted (TagList, reverse=True) :
            TagList_label.append(TagList[i])
            TagList_data.append(i)

        contestTimegood = []
        for i in (contestTime):
            t = time.strftime('%Y-%m-%d', time.localtime(i))
            #i = datetime.datetime.fromtimestamp(i).strftime('%c')
            contestTimegood.append(t)
            #print(t)
            #print(i)

        return render(request, 'userinfo/detail.html',
                      {
                      'exists': exists,
                      'contests_given': contests_given,
                      'name': name,
                      'rating': rating,
                      'contestTime':contestTime,
                      'contestTimegood':contestTimegood,
                      'ranks':ranks,
                      'newRatings':newRatings,
                      'bestRank': bestRank,
                      'TagList_data':TagList_data,
                      'TagList_label':TagList_label,
                      'ProbRatList_data':ProbRatList_data,
                      'ProbRatList_label':ProbRatList_label,
                      'TypeList_data':TypeList_data,
                      'TypeList_label':TypeList_label,
                      'VerdictList_data':VerdictList_data,
                      'VerdictList_label':VerdictList_label,
                      'LangList_data':LangList_data,
                      'LangList_label':LangList_label
                       }
                      )

def inputCompares(request):
    return render(request, 'userinfo/inputcompares.html')


def Compares(request):
    Firstuser = request.POST['Firstuser']
    Seconduser = request.POST['Seconduser']
    # rank,color,ar,institute,ac,wa,tle,rte,mle,challenged,cpe,skipped,ile,other = scrape(user)
    Firstverdict = scrape(Firstuser)
    Secondverdict = scrape(Seconduser)
    if Firstverdict == False or Secondverdict==False:
        Firstexists = Firstverdict
        Secondexists = Secondverdict
        return render(request, 'userinfo/compares.html',
                    {
                    'Secondexists': Secondexists,
                    'Firstexists': Firstexists
                    })

    else:
        # First User Verdict
        Firstexists = Firstverdict[0]
        Firstcontests_given = Firstverdict[1]
        Firstname = Firstverdict[2]
        Firstrating = Firstverdict[3]
        Firstmaxrating = Firstverdict[4]
        Firstcountry = Firstverdict[5]
        Firstcity = Firstverdict[6]
        Firstorganisation = Firstverdict[7]
        Firstrank = Firstverdict[8]
        Firstmaxrank = Firstverdict[9]

        FirstTagList = Firstverdict[10]
        FirstProbRatList = Firstverdict[11]
        FirstTypeList = Firstverdict[12]
        FirstLangList = Firstverdict[13]
        FirstVerdictList = Firstverdict[14]

        FirstcontestTime = Firstverdict[15]
        Firstranks = Firstverdict[16]
        FirstoldRatings = Firstverdict[17]
        FirstnewRatings = Firstverdict[18]
        FirstbestRank = Firstverdict[19]
        FirstworstRank = Firstverdict[20]

        # Second User Verdict

        Secondexists = Secondverdict[0]
        Secondcontests_given = Secondverdict[1]
        Secondname = Secondverdict[2]
        Secondrating = Secondverdict[3]
        Secondmaxrating = Secondverdict[4]
        Secondcountry = Secondverdict[5]
        Secondcity = Secondverdict[6]
        Secondorganisation = Secondverdict[7]
        Secondrank = Secondverdict[8]
        Secondmaxrank = Secondverdict[9]

        SecondTagList = Secondverdict[10]
        SecondProbRatList = Secondverdict[11]
        SecondTypeList = Secondverdict[12]
        SecondLangList = Secondverdict[13]
        SecondVerdictList = Secondverdict[14]

        SecondcontestTime = Secondverdict[15]
        Secondranks = Secondverdict[16]
        SecondoldRatings = Secondverdict[17]
        SecondnewRatings = Secondverdict[18]
        SecondbestRank = Secondverdict[19]
        SecondworstRank = Secondverdict[20]

        #First User verdicts changes

        Firstac=FirstVerdictList['OK']

        FirstVerdictList['Accepted'] = FirstVerdictList['OK']
        del FirstVerdictList['OK']


        FirstTypeList_label = []
        FirstTypeList_data = []

        for i in sorted (FirstTypeList) :
            FirstTypeList_data.append(FirstTypeList[i])
            FirstTypeList_label.append(i)

        FirstLangList_label = []
        FirstLangList_data = []

        for i in sorted (FirstLangList) :
            FirstLangList_data.append(FirstLangList[i])
            FirstLangList_label.append(i)

        FirstProbRatList_label = []
        FirstProbRatList_data = []

        for i in sorted (FirstProbRatList) :
            FirstProbRatList_data.append(FirstProbRatList[i])
            FirstProbRatList_label.append(i)

        FirstVerdictList_label = []
        FirstVerdictList_data = []

        FirstVerdictList = dict([(value, key) for key, value in FirstVerdictList.items()])
        for i in sorted (FirstVerdictList, reverse= True) :
            FirstVerdictList_label.append(FirstVerdictList[i])
            FirstVerdictList_data.append(i)

        FirstTagList_label = []
        FirstTagList_data = []

        FirstTagList = dict([(value, key) for key, value in FirstTagList.items()])
        for i in sorted (FirstTagList, reverse=True) :
            FirstTagList_label.append(FirstTagList[i])
            FirstTagList_data.append(i)

        FirstcontestTimegood = []
        for i in (FirstcontestTime):
            t = time.strftime('%Y-%m-%d', time.localtime(i))
            FirstcontestTimegood.append(t)

        #Second User verdicts changes

        Secondac=SecondVerdictList['OK']

        SecondVerdictList['Accepted'] = SecondVerdictList['OK']
        del SecondVerdictList['OK']


        SecondTypeList_label = []
        SecondTypeList_data = []

        for i in sorted (SecondTypeList) :
            SecondTypeList_data.append(SecondTypeList[i])
            SecondTypeList_label.append(i)

        SecondLangList_label = []
        SecondLangList_data = []

        for i in sorted (SecondLangList) :
            SecondLangList_data.append(SecondLangList[i])
            SecondLangList_label.append(i)

        SecondProbRatList_label = []
        SecondProbRatList_data = []

        for i in sorted (SecondProbRatList) :
            SecondProbRatList_data.append(SecondProbRatList[i])
            SecondProbRatList_label.append(i)

        SecondVerdictList_label = []
        SecondVerdictList_data = []

        SecondVerdictList = dict([(value, key) for key, value in SecondVerdictList.items()])
        for i in sorted (SecondVerdictList, reverse= True) :
            SecondVerdictList_label.append(SecondVerdictList[i])
            SecondVerdictList_data.append(i)

        SecondTagList_label = []
        SecondTagList_data = []

        SecondTagList = dict([(value, key) for key, value in SecondTagList.items()])
        for i in sorted (SecondTagList, reverse=True) :
            SecondTagList_label.append(SecondTagList[i])
            SecondTagList_data.append(i)

        SecondcontestTimegood = []
        for i in (SecondcontestTime):
            t = time.strftime('%Y-%m-%d', time.localtime(i))
            SecondcontestTimegood.append(t)

        #returning both user verdicts
        return render(request, 'userinfo/compares.html',
                      {
                      'Secondexists': Secondexists,
                      'Secondcontests_given': Secondcontests_given,
                      'Secondname': Secondname,
                      'Secondrating': Secondrating,
                      'SecondcontestTime':SecondcontestTime,
                      'SecondcontestTimegood':SecondcontestTimegood,
                      'Secondranks':Secondranks,
                      'SecondnewRatings':SecondnewRatings,
                      'SecondbestRank': SecondbestRank,
                      'SecondTagList_data':SecondTagList_data,
                      'SecondTagList_label':SecondTagList_label,
                      'SecondProbRatList_data':SecondProbRatList_data,
                      'SecondProbRatList_label':SecondProbRatList_label,
                      'SecondTypeList_data':SecondTypeList_data,
                      'SecondTypeList_label':SecondTypeList_label,
                      'SecondVerdictList_data':SecondVerdictList_data,
                      'VerdictList_label':SecondVerdictList_label,
                      'SecondLangList_data':SecondLangList_data,
                      'SecondLangList_label':SecondLangList_label,
                      'Firstexists': Firstexists,
                      'Firstcontests_given': Firstcontests_given,
                      'Firstname': Firstname,
                      'Firstrating': Firstrating,
                      'FirstcontestTime':FirstcontestTime,
                      'FirstcontestTimegood':FirstcontestTimegood,
                      'Firstranks':Firstranks,
                      'FirstnewRatings':FirstnewRatings,
                      'FirstbestRank': FirstbestRank,
                      'FirstTagList_data':FirstTagList_data,
                      'FirstTagList_label':FirstTagList_label,
                      'FirstProbRatList_data':FirstProbRatList_data,
                      'FirstProbRatList_label':FirstProbRatList_label,
                      'FirstTypeList_data':FirstTypeList_data,
                      'FirstTypeList_label':FirstTypeList_label,
                      'FirstVerdictList_data':FirstVerdictList_data,
                      'FirstVerdictList_label':FirstVerdictList_label,
                      'FirstLangList_data':FirstLangList_data,
                      'FirstLangList_label':FirstLangList_label
                       }
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
