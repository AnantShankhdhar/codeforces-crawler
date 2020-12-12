def scrape(username):
    import requests
    import json
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
        verdict_list={}
        prob_rat={}
        type_list={}
        lang_list={}

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

                #type_list
                type = problem['index']
                if type in type_list:
                    type_list[type]+=1
                else:
                    type_list[type]=1

        #Contests information
        contest_given=True
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

        else:
            contest_given=False
            return exists, contest_given, name, rating, maxrating, country, city, organization, rank, maxrank, tag_list, prob_rat, type_list, lang_list, verdict_list

        return exists,contest_given,name,rating,maxrating,country,city,organization,rank,maxrank,tag_list,prob_rat,type_list,lang_list,verdict_list,contest_time,ranks,oldratings,newratings,bestRank,worstRank
