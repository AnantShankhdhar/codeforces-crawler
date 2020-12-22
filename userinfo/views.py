from django.shortcuts import render,redirect
from .scraping import scrape,only_rating
from .teamrate import team_ratings
from .rank_color import rank_color
from .forms import SignUpForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
import time
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'userinfo/index.html')



def detail(request):
    user = request.POST['user']  # user is the name of the input
    # rank,color,ar,institute,ac,wa,tle,rte,mle,challenged,cpe,skipped,ile,other = scrape(user)
    colorslisttemp = ['rgba(255, 99, 132, 0.2)','rgba(54, 162, 235, 0.2)','rgba(255, 206, 86, 0.2)','rgba(75, 192, 192, 0.2)','rgba(153, 102, 255, 0.2)','rgba(255, 159, 64, 0.2)']
    colorsborderlisttemp = ['rgba(255, 99, 132, 1)','rgba(54, 162, 235, 1)','rgba(255, 206, 86, 1)','rgba(75, 192, 192, 1)','rgba(153, 102, 255, 1)','rgba(255, 159, 64, 1)']
    colorslist = []
    colorsborderlist = []
    for i in range(0,50,1):
        colorslist.append(colorslisttemp[i%6])
        colorsborderlist.append(colorsborderlisttemp[i%6])


    verdict = scrape(user)
    if verdict == False:
        exists = verdict
        messages.error(request, 'Username that you mentioned is incorrect.')
        return HttpResponseRedirect('../')
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

        VCList = verdict[21]
        RecentList = verdict[22]
        ProbRecommended = verdict[23]
        TagListAvg = verdict[24]
        FirstTimeChange = verdict[25]
        HeatmapList = verdict[26]
        HeatmapListAC = verdict[27]
        FirstTimeChangeExits=False
        if len(HeatmapList)==0:
            height=0
        else:
            height = (HeatmapList[0][0]-HeatmapList[len(HeatmapList)-1][0]+1)*175
        if('OK' in VerdictList):
            VerdictList['ACCEPTED'] = VerdictList['OK']
            del VerdictList['OK']
        else:
            pass


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

        VerdictList = dict(sorted(VerdictList.items(), key=lambda item: item[1],reverse=True))
        for i in VerdictList:
            VerdictList_label.append(i)
            VerdictList_data.append(VerdictList[i])

        TagList_label = []
        TagList_data = []

        TagList = dict(sorted(TagList.items(), key=lambda item: item[1], reverse=True))
        for i in TagList:
            TagList_label.append(i)
            TagList_data.append(TagList[i])

        TagListAvg_label = []
        TagListAvg_data = []

        TagListAvg = dict(sorted(TagListAvg.items(), key=lambda item: item[1], reverse=True))
        for i in TagListAvg:
            TagListAvg_label.append(i)
            TagListAvg_data.append(TagListAvg[i])

        return  render(request, 'userinfo/detail.html',
                       {'user':user,
                       'maxrating':maxrating,
                       'country':country,
                       'city':city,
                       'organisation':organisation,
                       'rank':rank,
                       'maxrank':maxrank,
                       'exists': exists,
                       'contests_given': contests_given,
                       'name': name,
                       'rating': rating,
                       'TagList': TagList,
                       'TagList_data':TagList_data,
                       'TagList_label':TagList_label,
                       'TagListAvg_data':TagListAvg_data,
                       'TagListAvg_label':TagListAvg_label,
                       'VCList':VCList,
                       'RecentList':RecentList,
                       'ProbRecommended':ProbRecommended,
                       'TagListAvg':TagListAvg,
                       'ProbRatList_data':ProbRatList_data,
                       'ProbRatList_label':ProbRatList_label,
                       'TypeList_data':TypeList_data,
                       'TypeList_label':TypeList_label,
                       'VerdictList_data':VerdictList_data,
                       'VerdictList_label':VerdictList_label,
                       'LangList_data':LangList_data,
                       'LangList_label':LangList_label,
                       'colorslist': colorslist,
                       'colorsborderlist':colorsborderlist,
                       'FirstTimeChangeExits':FirstTimeChangeExits,
                       'HeatmapList':HeatmapList,
                       'HeatmapListAC':HeatmapListAC,
                       'height':height
                        }
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

        VCList = verdict[21]
        RecentList = verdict[22]
        ProbRecommended = verdict[23]
        TagListAvg = verdict[24]
        FirstTimeChange = verdict[25]
        HeatmapList = verdict[26]
        HeatmapListAC = verdict[27]
        FirstTimeChangeExits=True

        rank, passrankcolor = rank_color(rating)

        userfirstletter = user[0]
        userremaining = user[1:]

        if ('OK' in VerdictList):
            VerdictList['ACCEPTED'] = VerdictList['OK']
            del VerdictList['OK']
        else:
            pass


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

        VerdictList = dict(sorted(VerdictList.items(), key=lambda item: item[1],reverse=True))
        for i in VerdictList:
            VerdictList_label.append(i)
            VerdictList_data.append(VerdictList[i])

        TagList_label = []
        TagList_data = []

        TagList = dict(sorted(TagList.items(), key=lambda item: item[1], reverse=True))
        for i in TagList:
            TagList_label.append(i)
            TagList_data.append(TagList[i])

        TagListAvg_label = []
        TagListAvg_data = []

        TagListAvg = dict(sorted(TagListAvg.items(), key=lambda item: item[1], reverse=True))
        for i in TagListAvg:
            TagListAvg_label.append(i)
            TagListAvg_data.append(TagListAvg[i])

        contestTimegood = []
        for i in (contestTime):
            t = time.strftime('%Y-%m-%d', time.localtime(i))
            #i = datetime.datetime.fromtimestamp(i).strftime('%c')
            contestTimegood.append(t)
        height = (HeatmapList[0][0]-HeatmapList[len(HeatmapList)-1][0]+1)*175
        return render(request, 'userinfo/detail.html',
                      {
                      'user':user,
                      'maxrating':maxrating,
                      'country':country,
                      'city':city,
                      'organisation':organisation,
                      'rank':rank,
                      'maxrank':maxrank,
                      'exists': exists,
                      'contests_given': contests_given,
                      'name': name,
                      'rating': rating,
                      'contestTime':contestTime,
                      'contestTimegood':contestTimegood,
                      'ranks':ranks,
                      'newRatings':newRatings,
                      'bestRank': bestRank,
                      'TagList': TagList,
                      'TagList_data':TagList_data,
                      'TagList_label':TagList_label,
                      'TagListAvg_data':TagListAvg_data,
                      'TagListAvg_label':TagListAvg_label,
                      'VCList':VCList,
                      'RecentList':RecentList,
                      'ProbRecommended':ProbRecommended,
                      'TagListAvg':TagListAvg,
                      'ProbRatList_data':ProbRatList_data,
                      'ProbRatList_label':ProbRatList_label,
                      'TypeList_data':TypeList_data,
                      'TypeList_label':TypeList_label,
                      'VerdictList_data':VerdictList_data,
                      'VerdictList_label':VerdictList_label,
                      'LangList_data':LangList_data,
                      'LangList_label':LangList_label,
                      'FirstTimeChange':FirstTimeChange,
                      'colorslist': colorslist,
                      'colorsborderlist':colorsborderlist,
                      'FirstTimeChangeExits':FirstTimeChangeExits,
                      'HeatmapList':HeatmapList,
                      'passrankcolor':passrankcolor,
                      'userfirstletter':userfirstletter,
                      'userremaining':userremaining,
                      'HeatmapListAC':HeatmapListAC,
                      'height':height
                       }
                      )

def Compares(request):
    error = False

    #colorslist for charts
    colorslisttemp = ['rgba(255, 99, 132, 0.2)','rgba(54, 162, 235, 0.2)','rgba(255, 206, 86, 0.2)','rgba(75, 192, 192, 0.2)','rgba(153, 102, 255, 0.2)','rgba(255, 159, 64, 0.2)']
    colorsborderlisttemp = ['rgba(255, 99, 132, 1)','rgba(54, 162, 235, 1)','rgba(255, 206, 86, 1)','rgba(75, 192, 192, 1)','rgba(153, 102, 255, 1)','rgba(255, 159, 64, 1)']
    colorslist = []
    colorsborderlist = []
    for i in range(0,50,1):
        colorslist.append(colorslisttemp[i%6])
        colorsborderlist.append(colorsborderlisttemp[i%6])

    try:
        Firstuser = request.POST['Firstuser']
    except:
        error = True
    try:
        Seconduser = request.POST['Seconduser']
    except:
        error = True
    if error == True:
        messages.error(request, 'Please Enter both username to Compare.')
        return HttpResponseRedirect('../')

    Fverdict=scrape(Firstuser)
    Sverdict=scrape(Seconduser)

    if Fverdict == False or Sverdict == False:
        messages.error(request, 'One of the Username that you mentioned is incorrect.')
        return HttpResponseRedirect('../')

    else:
        Fexists = Fverdict[0]
        Fcontests_given = Fverdict[1]
        Fname = Fverdict[2]
        Frating = Fverdict[3]
        Fmaxrating = Fverdict[4]
        Fcountry = Fverdict[5]
        Fcity = Fverdict[6]
        Forganisation = Fverdict[7]
        Frank = Fverdict[8]
        Fmaxrank = Fverdict[9]

        FTagList = Fverdict[10]
        FProbRatList = Fverdict[11]
        FTypeList = Fverdict[12]
        FLangList = Fverdict[13]
        FVerdictList = Fverdict[14]

        FcontestTime = Fverdict[15]
        Franks = Fverdict[16]
        FoldRatings = Fverdict[17]
        FnewRatings = Fverdict[18]
        FbestRank = Fverdict[19]
        FworstRank = Fverdict[20]

        FVCList = Fverdict[21]
        FRecentList = Fverdict[22]
        FProbRecommended = Fverdict[23]
        FTagListAvg = Fverdict[24]
        FFirstTimeChange = Fverdict[25]

        Sexists = Sverdict[0]
        Scontests_given = Sverdict[1]
        Sname = Sverdict[2]
        Srating = Sverdict[3]
        Smaxrating = Sverdict[4]
        Scountry = Sverdict[5]
        Scity = Sverdict[6]
        Sorganisation = Sverdict[7]
        Srank = Sverdict[8]
        Smaxrank = Sverdict[9]

        STagList = Sverdict[10]
        SProbRatList = Sverdict[11]
        STypeList = Sverdict[12]
        SLangList = Sverdict[13]
        SVerdictList = Sverdict[14]

        ScontestTime = Sverdict[15]
        Sranks = Sverdict[16]
        SoldRatings = Sverdict[17]
        SnewRatings = Sverdict[18]
        SbestRank = Sverdict[19]
        SworstRank = Sverdict[20]

        SVCList = Sverdict[21]
        SRecentList = Sverdict[22]
        SProbRecommended = Sverdict[23]
        STagListAvg = Sverdict[24]
        SFirstTimeChange = Sverdict[25]

        if ('OK' in FVerdictList):
            FVerdictList['ACCEPTED'] = FVerdictList['OK']
            del FVerdictList['OK']
        else:
            pass

        if ('OK' in SVerdictList):
            SVerdictList['ACCEPTED'] = SVerdictList['OK']
            del SVerdictList['OK']
        else:
            pass

        Frank, Fpassrankcolor = rank_color(Frating)

        Fuserfirstletter = Firstuser[0]
        Fuserremaining = Firstuser[1:]

        Srank, Spassrankcolor = rank_color(Srating)

        Suserfirstletter = Seconduser[0]
        Suserremaining = Seconduser[1:]


        #Combine
        CTypeList_label = []
        FTypeList_data = []
        STypeList_data = []
        for i in sorted(FTypeList):
            CTypeList_label.append(i)
        for i in sorted(STypeList):
            if i not in CTypeList_label:
                CTypeList_label.append(i)
        CTypeList_label.sort()
        for i in CTypeList_label:
            if i in FTypeList:
                FTypeList_data.append(FTypeList[i])
            else:
                FTypeList_data.append(0)
            if i in STypeList:
                STypeList_data.append(STypeList[i])
            else:
                STypeList_data.append(0)
        # print(CTypeList_label)
        # print(FTypeList_data)
        # print(STypeList_data)


        #Not combine
        FLangList_label = []
        FLangList_data = []
        for i in sorted(FLangList):
            FLangList_data.append(FLangList[i])
            FLangList_label.append(i)
        SLangList_label = []
        SLangList_data = []
        for i in sorted(SLangList):
            SLangList_data.append(SLangList[i])
            SLangList_label.append(i)

        #Combine
        CProbRatList_label = []
        FProbRatList_data = []
        SProbRatList_data = []
        for i in sorted(FProbRatList):
            CProbRatList_label.append(i)
        for i in sorted(SProbRatList):
            if i not in CProbRatList_label:
                CProbRatList_label.append(i)
        CProbRatList_label.sort()
        for i in CProbRatList_label:
            if i in FProbRatList:
                FProbRatList_data.append(FProbRatList[i])
            else:
                FProbRatList_data.append(0)
            if i in SProbRatList:
                SProbRatList_data.append(SProbRatList[i])
            else:
                SProbRatList_data.append(0)

        #Combine
        CVerdictList_label = []
        FVerdictList_data = []
        SVerdictList_data = []
        FVerdictList = dict(sorted(FVerdictList.items(), key=lambda item: item[1], reverse=True))
        SVerdictList = dict(sorted(SVerdictList.items(), key=lambda item: item[1], reverse=True))
        for i in FVerdictList:
            CVerdictList_label.append(i)
        for i in sorted(SVerdictList):
            if i not in CVerdictList_label:
                CVerdictList_label.append(i)
        for i in CVerdictList_label:
            if i in FVerdictList:
                FVerdictList_data.append(FVerdictList[i])
            else:
                FVerdictList_data.append(0)
            if i in SVerdictList:
                SVerdictList_data.append(SVerdictList[i])
            else:
                SVerdictList_data.append(0)


        #Combine
        CTagList_label = []
        FTagList_data = []
        STagList_data = []
        FTagList = dict(sorted(FTagList.items(), key=lambda item: item[1], reverse=True))
        STagList = dict(sorted(STagList.items(), key=lambda item: item[1], reverse=True))
        for i in FTagList:
            CTagList_label.append(i)
        for i in sorted(STagList):
            if i not in CTagList_label:
                CTagList_label.append(i)
        for i in CTagList_label:
            if i in FTagList:
                FTagList_data.append(FTagList[i])
            else:
                FTagList_data.append(0)
            if i in STagList:
                STagList_data.append(STagList[i])
            else:
                STagList_data.append(0)


        #Combine
        CTagListAvg_label = []
        FTagListAvg_data = []
        STagListAvg_data = []
        FTagListAvg = dict(sorted(FTagListAvg.items(), key=lambda item: item[1], reverse=True))
        STagListAvg = dict(sorted(STagListAvg.items(), key=lambda item: item[1], reverse=True))
        for i in FTagListAvg:
            CTagListAvg_label.append(i)
        for i in sorted(STagListAvg):
            if i not in CTagListAvg_label:
                CTagListAvg_label.append(i)
        for i in CTagListAvg_label:
            if i in FTagListAvg:
                FTagListAvg_data.append(FTagListAvg[i])
            else:
                FTagListAvg_data.append(0)
            if i in STagListAvg:
                STagListAvg_data.append(STagListAvg[i])
            else:
                STagListAvg_data.append(0)


        FcontestTimegood = []
        ScontestTimegood = []
        for i in (FcontestTime):
            t = time.strftime('%Y-%m-%d', time.localtime(i))
            # i = datetime.datetime.fromtimestamp(i).strftime('%c')
            FcontestTimegood.append(t)
        for i in (ScontestTime):
            t = time.strftime('%Y-%m-%d', time.localtime(i))
            # i = datetime.datetime.fromtimestamp(i).strftime('%c')
            ScontestTimegood.append(t)

        return render(request, 'userinfo/compares.html',
                      {
                      'Spassrankcolor':Spassrankcolor,
                      'Suserfirstletter':Suserfirstletter,
                      'Suserremaining':Suserremaining,
                      'Fpassrankcolor':Fpassrankcolor,
                      'Fuserfirstletter':Fuserfirstletter,
                      'Fuserremaining':Fuserremaining,
                        'Firstuser':Firstuser,
                        'Seconduser':Seconduser,
                        'Fexists':Fexists,
                        'Fcontests_given':Fcontests_given,
                        'Fname':Fname,
                        'Frating':Frating ,
                        'Fmaxrating':Fmaxrating,
                        'Fcountry':Fcountry,
                        'Fcity':Fcity ,
                        'Forganisation':Forganisation ,
                        'Frank':Frank,
                        'Fmaxrank':Fmaxrank,
                        'Sexists':Sexists,
                        'Scontests_given':Scontests_given,
                        'Sname':Sname,
                        'Srating':Srating ,
                        'Smaxrating':Smaxrating ,
                        'Scountry':Scountry,
                        'Scity':Scity ,
                        'Sorganisation':Sorganisation ,
                        'Srank':Srank,
                        'Smaxrank':Smaxrank,
                        'CTypeList_label':CTypeList_label,
                        'FTypeList_data':FTypeList_data,
                        'STypeList_data':STypeList_data,
                        'FLangList_label':FLangList_label,
                        'FLangList_data':FLangList_data,
                        'SLangList_label':SLangList_label,
                        'SLangList_data':SLangList_data,
                        'CVerdictList_label':CVerdictList_label,
                        'FVerdictList_data':FVerdictList_data,
                        'SVerdictList_data':SVerdictList_data,
                        'CTagList_label':CTagList_label,
                        'FTagList_data':FTagList_data,
                        'STagList_data':STagList_data,
                        'CProbRatList_label':CProbRatList_label,
                        'FProbRatList_data':FProbRatList_data,
                        'SProbRatList_data':SProbRatList_data,
                        'CTagListAvg_label':CTagListAvg_label,
                        'FTagListAvg_data':FTagListAvg_data,
                        'STagListAvg_data':STagListAvg_data,
                        'FcontestTimegood':FcontestTimegood,
                        'ScontestTimegood':ScontestTimegood,
                        'Franks':Franks,
                        'Sranks':Sranks,
                        'FnewRatings': FnewRatings,
                        'SnewRatings':SnewRatings,
                        'colorslist': colorslist,
                        'colorsborderlist':colorsborderlist
                      }
                      )


def teamrate(request):
    users=[]
    try:
        user1 = request.POST['user1']
        if user1 != '':
            users.append(user1)
    except:
        pass
    try:
        user2 = request.POST['user2']
        if user2 != '':
            users.append(user2)
    except:
        pass
    try:
        user3 = request.POST['user3']
        if user3 != '':
            users.append(user3)
    except:
        pass
    try:
        user4 = request.POST['user4']
        if user4 != '':
            users.append(user4)
    except:
        pass

    if(len(users)==0):
        errorMsg="Provide atleast 1 valid input"
        return render(request,'userinfo/index.html',
                    {'error':errorMsg})
    verdict=only_rating(users)
    Exists=verdict[0]
    if len(Exists)==0:
        errorMsg="Provide atleast 1 valid input"
        return render(request,'userinfo/index.html',
                    {'error':errorMsg})

    NotExists=verdict[1]
    UsersRating=verdict[2]
    answer=team_ratings(UsersRating)

    length=len(NotExists)
    rank,color=rank_color(answer)
    return render(request, 'userinfo/teamrate.html',
                  {
                   'length':length,
                   'notexists':NotExists,
                   'answer':answer,
                   'rank':rank,
                   'color':color,
                   'exists':Exists})




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
