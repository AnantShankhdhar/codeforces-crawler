def only_rating(users):
    import requests
    import json
    api_url = "https://codeforces.com/api/"

    exists=[]
    not_exists=[]
    users_rating=[]
    for user in users:
        info = requests.get(api_url + "user.info?handles=" + user)
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
    exists = True
    api_url = "https://codeforces.com/api/"

    info = requests.get(api_url + "user.info?handles=" + username)

    if(info.json()['status']!='OK'):
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
            organization = "organisation not mentioned"
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

        submissions = requests.get(api_url + "user.status?handle=" + username)
        submissions_results = submissions.json()['result']
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

            if verdict == 'OK':
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
                contestId = problem['contestId']
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
            k=k/100
            if(k-math.floor(k)>0.5):
                tag_list_avg[tags]=math.floor(k)*100+100
            else:
                tag_list_avg[tags]=math.floor(k)*100

        sort_tag_list=tag_list_avg
        sort_tag_list=dict(sorted(sort_tag_list.items(), key=lambda item: item[1]))
        for tag in sort_tag_list:
            weak_tag_list[tag]=sort_tag_list[tag]
            if len(weak_tag_list)==10:
                break

        #Problem recommendation
        #prob_list contains all solved
        prob_recommended=[]

        for weak_tag in weak_tag_list:
            all_prob = requests.get(api_url + "problemset.problems?tags="+weak_tag)
            all_prob_result=all_prob.json()['result']['problems']
            for prob in all_prob_result:
                contestId=prob['contestId']
                index=prob['index']
                ID=str(contestId)+index
                try:
                    prob_rating=prob['rating']
                    prob_name=prob['name']
                    if (ID not in prob_list) and (abs(rating-prob_rating)<=200 or rating<=800):
                        prob_recommended.append([prob_name,contestId,index])
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
        contest_list=[]
        ratings = requests.get(api_url + "user.rating?handle=" + username)
        rating_results = ratings.json()['result']
        if len(rating_results)!=0:
            bestRank=1e10
            worstRank=1
            contest_time = []
            ranks = []
            oldratings = []
            newratings = []
            for result in rating_results:
                contest_time.append(result['ratingUpdateTimeSeconds'])
                ranks.append(result['rank'])
                bestRank=min(bestRank,result['rank'])
                worstRank=max(worstRank,result['rank'])
                oldratings.append(result['oldRating'])
                newratings.append(result['newRating'])
                #contest_list.append(result['contestId'])

        else:
            contest_given=False

        #VC recommendation
        #contest_list has all given contests
        # prob_list_contest contains contest with atleast one solved
        vc_list=[]
        all_contest = requests.get(api_url + "contest.list?gym=false")
        all_contest_results = all_contest.json()['result']
        for i in range(len(all_contest_results)):
            if i%5==0:
                contestId=all_contest_results[i]['id']
                if (contestId not in prob_list_contest):
                    contest_name=all_contest_results[i]['name']
                    vc_list.append([contest_name,contestId])
                    if len(vc_list)==5:
                        break

        if contest_given==False:
            return exists, contest_given, name, rating, maxrating, country, city, organization, rank, maxrank, tag_list, prob_rat, type_list, lang_list, verdict_list,vc_list,recent_list,prob_recommended,tag_list_avg

        print("vc_list=",vc_list)
        print("recent_list=",recent_list)
        print("prob_recommended=",prob_recommended)
        print("tag_list_avg=",tag_list_avg)
        return exists,contest_given,name,rating,maxrating,country,city,organization,rank,maxrank,tag_list,prob_rat,type_list,lang_list,verdict_list,contest_time,ranks,oldratings,newratings,bestRank,worstRank,vc_list,recent_list,prob_recommended,tag_list_avg
