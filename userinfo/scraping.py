def only_rating(users):
    import requests
    import json
    api_url = "https://codeforces.com/api/"
    headers = {'Accept': 'application/json'}

    exists=[]
    not_exists=[]
    users_rating=[]
    for user in users:
        info = requests.get(api_url + "user.info?handles=" + user, headers=headers)
        if (info.json()['status'] != 'OK'):
            not_exists.append(user)
        else:
            info_results = info.json()['result'][0]
            exists.append(user)
            try:
                rating = info_results['rating']
            except:
                rating = 0
            users_rating.append(rating)

    return exists,not_exists,users_rating

def scrape(username):
    import requests
    import json
    import math
    import datetime
    import time
    exists = True
    api_url = "https://codeforces.com/api/"
    headers = {'Accept': 'application/json'}

    info = requests.get(api_url + "user.info?handles=" + username, headers=headers)
    try:
        user_status = info.json()['status']
    except:
        user_status = ''

    if user_status != 'OK':
        exists = False
        return exists
    else:
        info_results = info.json()['result'][0]
        try:
            name = info_results['firstName'] + " " + info_results['lastName']
        except:
            name = "Name not mentioned"
        try:
            rating = info_results['rating']
        except:
            rating = 0
        try:
            maxrating = info_results['maxRating']
        except:
            maxrating = 0
        try:
            country = info_results['country']
        except:
            country = "Country not mentioned"
        try:
            city = info_results['city']
        except:
            city = "City not mentioned"
        try:
            organization = info_results['organization']
        except:
            organization = "Organisation not mentioned"
        try:
            rank = info_results['rank']
        except:
            rank = "Unrated"
        try:
            maxrank = info_results['maxRank']
        except:
            maxrank = "Unrated"

        tag_list={}
        tag_list_count={}
        tag_list_sum={}
        tag_list_avg={}
        sort_tag_list={}
        weak_tag_list={}
        verdict_list={}
        prob_rat={}
        type_list={}
        lang_list={}
        prob_list=[]
        prob_list_contest=[]

        heatmap_list={}
        heatmap_list_ac={}

        submissions = requests.get(api_url + "user.status?handle=" + username, headers=headers)
        try:
            submissions_results = submissions.json()['result']
        except:
            submissions_results = []
        for result in submissions_results:
            #verdict
            verdict=result['verdict']
            if verdict in verdict_list:
                verdict_list[verdict]+=1
            else:
                verdict_list[verdict]=1

            #language
            language = result['programmingLanguage']
            if language in lang_list:
                lang_list[language]+=1
            else:
                lang_list[language]=1

            #submission time
            sub_time=result['creationTimeSeconds']
            sub_date= datetime.datetime.fromtimestamp(sub_time)
            time_id=str(sub_date.year)+" "+str(sub_date.month)+" "+str(sub_date.day)
            if time_id in heatmap_list:
                heatmap_list[time_id]+=1
            else:
                heatmap_list[time_id]=1

            if verdict == 'OK':
                #submission time
                if time_id in heatmap_list_ac:
                    heatmap_list_ac[time_id] += 1
                else:
                    heatmap_list_ac[time_id] = 1

                #tags
                problem = result['problem']
                tags = problem['tags']
                for tags_obj in tags:
                    try:
                        rat=problem['rating']
                        if tags_obj in tag_list_count:
                            tag_list_count[tags_obj] += 1
                            tag_list_sum[tags_obj] += rat
                        else:
                            tag_list_count[tags_obj] = 1
                            tag_list_sum[tags_obj] = rat
                    except:
                        pass

                    if tags_obj in tag_list:
                        tag_list[tags_obj]+=1
                    else:
                        tag_list[tags_obj]=1

                #rating
                try:
                    rat=problem['rating']
                    if rat in prob_rat:
                        prob_rat[rat]+=1
                    else:
                        prob_rat[rat]=1

                except:
                    pass
                type = problem['index']
                try:
                    contestId = problem['contestId']
                except:
                    pass
                prob_list.append(str(contestId)+type)
                if contestId not in prob_list_contest:
                    prob_list_contest.append(contestId)

                #type_list
                type = problem['index'][0]
                if type in type_list:
                    type_list[type]+=1
                else:
                    type_list[type]=1

        for tags in tag_list_count:
            k=(tag_list_sum[tags])/(tag_list_count[tags])
            tag_list_avg[tags]=int(k)

        sort_tag_list=tag_list_avg
        sort_tag_list=dict(sorted(sort_tag_list.items(), key=lambda item: item[1]))
        for tag in sort_tag_list:
            weak_tag_list[tag]=sort_tag_list[tag]
            if len(weak_tag_list)==10:
                break

        #Problem recommendation
        #prob_list contains all solved
        prob_recommended=[]
        weak10=['greedy','math','implementation','constructive algorithms','brute force','dp','sortings','data structures','graphs','binary search']
        j=0
        while len(weak_tag_list)<10:
            if weak10[j] not in weak_tag_list:
                weak_tag_list[weak10[j]]=1
            j+=1

        for weak_tag in weak_tag_list:
            all_prob = requests.get(api_url + "problemset.problems?tags="+weak_tag, headers=headers)
            try:
                all_prob_result=all_prob.json()['result']['problems']
            except:
                all_prob_result = []
            for prob in all_prob_result:
                contestId=prob['contestId']
                index=prob['index']
                ID=str(contestId)+index
                try:
                    prob_rating=prob['rating']
                    prob_name=prob['name']
                    if (ID not in prob_list) and (abs(rating-prob_rating)<=200 or (rating<=800 and prob_rating<=1000) or (rating>=3500 and prob_rating>=3300)):
                        prob_recommended.append([prob_name,contestId,index])
                        prob_list.append(ID)
                        break
                except:
                    pass

        #Recent problems
        recent_list = []
        for result in submissions_results:
            # verdict
            verdict = result['verdict']
            problem = result['problem']
            if verdict == 'OK':
                try:
                    rat = problem['rating']
                except:
                    pass

                type = problem['index']
                prob_name = problem['name']
                contestId = problem['contestId']
                recent_list.append([prob_name,rat,str(contestId),type])

            if(len(recent_list)==10):
                break

        #Contests information
        contest_given=True
        cutoffs=[0,1200,1400,1600,1900,2100,2300,2400,2600,3000,5000]
        flag=[0,0,0,0,0,0,0,0,0,0]
        became=["Newbie","Pupil","Specialist","Expert","Candidate Master","Master","International Master","Grandmaster","International Grandmaster","Legendary Grandmaster"]
        first_time_change=[]

        ratings = requests.get(api_url + "user.rating?handle=" + username, headers=headers)
        try:
            rating_results = ratings.json()['result']
        except:
            rating_results = []
        if len(rating_results)!=0:
            bestRank=1e10
            worstRank=1
            contest_time = []
            ranks = []
            oldratings = []
            newratings = []
            it=0
            for result in rating_results:
                contest_time.append(result['ratingUpdateTimeSeconds'])
                ranks.append(result['rank'])
                bestRank=min(bestRank,result['rank'])
                worstRank=max(worstRank,result['rank'])
                oldratings.append(result['oldRating'])
                newratings.append(result['newRating'])
                it+=1
                for i in range(10):
                    if (result['newRating']>=cutoffs[i]) and (result['newRating']<cutoffs[i+1]) and (flag[i]==0):
                        flag[i]=1
                        first_time_change.append("Became "+became[i]+" in contest "+str(it))
                        # print("Became ",became[i]," in contest ",it)

        else:
            contest_given=False

        #heatmap
        heatMapListac = []
        for k, v in heatmap_list_ac.items():
            x = k.split()
            sub = [int(x[0]), int(x[1]), int(x[2]), v]
            heatMapListac.append(sub)
        heatMapList = []
        for k, v in heatmap_list.items():
            x = k.split()
            sub = [int(x[0]), int(x[1]), int(x[2]), v]
            heatMapList.append(sub)

        #VC recommendation
        #contest_list has all given contests
        # prob_list_contest contains contest with atleast one solved
        vc_list=[]
        all_contest = requests.get(api_url + "contest.list?gym=false", headers=headers)
        try:
            all_contest_results = all_contest.json()['result']
        except:
            all_contest_results = []
        for i in range(len(all_contest_results)):
            if i%4==0 and i>12:
                contestId=all_contest_results[i]['id']
                phase=all_contest_results[i]['phase']
                contest_name = all_contest_results[i]['name']
                if (contestId not in prob_list_contest) and (phase == "FINISHED") and (contest_name[0:10]=="Codeforces" or contest_name[0:11]=="Educational"):
                    if (contest_name[23:29]=="Div. 4"):
                        continue
                    if (rating<=1599 and contest_name[23:29]=="Div. 1"):
                        continue
                    if (rating>=1900 and contest_name[23:29]=="Div. 3"):
                        continue
                    if (rating>=2100 and (contest_name[23:29]=="Div. 2" or contest_name[0:11]=="Educational")):
                        continue
                    vc_list.append([contest_name,contestId])
                    if len(vc_list)==5:
                        break
        
        

        if contest_given==False:
            return exists, contest_given, name, rating, maxrating, country, city, organization, rank, maxrank, tag_list, prob_rat, type_list, lang_list, verdict_list,[],[],[],[],0,0,vc_list,recent_list,prob_recommended,tag_list_avg,[],heatMapList,heatMapListac

        return exists,contest_given,name,rating,maxrating,country,city,organization,rank,maxrank,tag_list,prob_rat,type_list,lang_list,verdict_list,contest_time,ranks,oldratings,newratings,bestRank,worstRank,vc_list,recent_list,prob_recommended,tag_list_avg,first_time_change,heatMapList,heatMapListac
