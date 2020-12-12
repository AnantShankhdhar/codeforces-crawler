# Using bs4 to scrap, not in use

from userinfo.models import Question, ContestDb


def scrape(username):
    import requests
    import json
    exists = True

    # For contest database
    import datetime
    contests_link = 'https://codeforces.com/contests'
    rq = requests.get(contests_link)
    from bs4 import BeautifulSoup
    chsoup = BeautifulSoup(rq.text, "lxml")
    page = chsoup.find('div', attrs={'class': 'pagination'}).find_all('span', attrs={'class': 'page-index'})[-1].string
    flag = 0
    for i in range(int(page)):
        page_link = 'https://codeforces.com/contests/page/' + str(i + 1)
        rq1 = requests.get(page_link)
        cpgsoup = BeautifulSoup(rq1.text, "lxml")
        crows = cpgsoup.find_all('table')[1].find_all('tr')[1:]
        for crow in crows:
            rowinfo = crow.find_all('td')
            cname = rowinfo[0]
            for child in cname.children:
                contest_name = child
                break
            contest_name = contest_name.strip()
            date = rowinfo[2].find('span', attrs={'class': 'format-date'}).string[0:11]
            year = int(date[7:])
            month = date[0:3]
            if (month == 'Jan'):
                month = 1
            elif (month == 'Feb'):
                month = 2
            elif (month == 'Mar'):
                month = 3
            elif (month == 'Apr'):
                month = 4
            elif (month == 'May'):
                month = 5
            elif (month == 'Jun'):
                month = 6
            elif (month == 'Jul'):
                month = 7
            elif (month == 'Aug'):
                month = 8
            elif (month == 'Sep'):
                month = 9
            elif (month == 'Oct'):
                month = 10
            elif (month == 'Nov'):
                month = 11
            elif (month == 'Dec'):
                month = 12
            day = int(date[4:6])
            for object in ContestDb.objects.all():
                if (object.contest_name == contest_name):
                    flag = 1
                    break
            if (flag == 1):
                break
            else:
                contest_obj = ContestDb(contest_name=contest_name, date=datetime.datetime(year, month, day))
                contest_obj.save()
        if (flag == 1):
            break

    try:
        profile = "https://codeforces.com/profile/" + str(username)
        sub = "https://codeforces.com/submissions/" + str(username)
        r1 = requests.get(profile)
        r2 = requests.get(sub)
        # from bs4 import BeautifulSoup
        profilesoup = BeautifulSoup(r1.text, "lxml")
        subsoup = BeautifulSoup(r2.text, "lxml")
        info = profilesoup.find('div', attrs={'class': 'info'})
        maininfo = info.find('div', attrs={'class': 'main-info'})
        userrank = maininfo.find('div', attrs={'class': 'user-rank'})  # fine
        rank = userrank.find('span').string  # Rank

        color = userrank.find('span').get('class')
        for c in color:
            color = c[5:]  # Color
        ar = ''
        try:
            details = maininfo.find('div', attrs={'style': 'margin-top: 0.5em;'})  # problem
            detail = details.find('div', attrs={'style': 'font-size: 0.8em; color: #777;'})
            for child in detail.children:
                ar = ar + (child.string)
        except:
            ar += "No info"
        try:
            detail1 = detail.find_next_sibling()
            institute = detail1.find('a').string  # institute
        except:
            institute = "Institute not mentioned"
        try:
            rating = info.find('ul').find('li').find('span').string  # rating
        except:
            rating = "Not given any contest"

        # try:
        #     pg=subsoup.find_all('div',attrs={'class':'pagination'})[1].find('ul').find_all('li')[-2].find('a').string  #pages
        # except:
        #     pg=1

        tag_list = {}
        verdict_list = {}
        prob_rat = []
        type_list = {}
        lang_list = {}

        api_url = "https://codeforces.com/api/"

        submissions = requests.get(api_url + "user.status?handle=" + username)
        results = submissions.json()['result']
        for result in results:
            # verdict
            verdict = result['verdict']
            if verdict in verdict_list:
                verdict_list[verdict] += 1
            else:
                verdict_list[verdict] = 1

            # language
            language = result['programmingLanguage']
            if language in lang_list:
                lang_list[language] += 1
            else:
                lang_list[language] = 1

            if verdict == 'OK':
                # tags
                problem = result['problem']
                tags = problem['tags']
                for tags_obj in tags:
                    if tags_obj in tag_list:
                        tag_list[tags_obj] += 1
                    else:
                        tag_list[tags_obj] = 1

                # rating
                prob_rat.append(problem['rating'])

                # type_list
                type = problem['index']
                if type in type_list:
                    type_list[type] += 1
                else:
                    type_list[type] = 1

        for i in range(int(pg)):
            subpg="https://codeforces.com/submissions/"+str(username)+"/page/"+str(i+1)
            r3=requests.get(subpg)
            subpgsoup=BeautifulSoup(r3.text,"lxml")
            try:
                acc=subpgsoup.find_all('span',attrs={'class':'verdict-accepted'})
                ac=ac+len(acc)
                rej=subpgsoup.find_all('span',attrs={'class':'verdict-rejected'})
                for re in rej:
                    ant=re.contents[0]
                    if(ant[0:12]=='Wrong answer'):
                        wa=wa+1
                    elif(ant[0:10]=='Time limit'):
                        tle=tle+1
                    elif(ant[0:13]=='Runtime error'):
                        rte=rte+1
                    elif(ant[0:12]=='Memory limit'):
                        mle=mle+1
                    elif(ant[0:10]=='Challenged'):
                        challenged=challenged+1
                    elif(ant[0:7]=='Skipped'):
                        skipped=skipped+1
                    elif(ant[0:8]=='Idleness'):
                        ile=ile+1
                    else:
                        other=other+1

                ce=subpgsoup.find_all('span',attrs={'submissionverdict':'COMPILATION_ERROR'})
                cpe=len(ce)
                prob=subpgsoup.find_all('tr')
                for pro in prob:
                    pr=pro.find('span',attrs={'class':'verdict-accepted'})
                    try:
                        lang=pro.find_all('td')[4]
                        if(lang!=None):
                            lang_list.append(lang.string.strip())
                    except:
                        pass

                    if(pr!=None):
                        ques=pro.find_all('a')[-1]
                        ql=ques.get('href')
                        qlink='https://codeforces.com'+str(ql)
                        link_list.append(qlink)
                        new_l=set(link_list)
                        new_list=list(new_l)
            except:
                pass

        try:
            for ele in new_list:
                flag = 0
                for object in Question.objects.all():
                    if(object.prob_link == ele):
                        flag=1
                        type_list.append(object.prob_level)
                        prob_rat.append(object.prob_rat)
                        if(object.special_problem==True):
                            special_problem+=1
                        if(object.expression_parsing==True):
                            expression_parsing+=1
                        if(object.fft==True):
                            fft += 1
                        if (object.two_pointers == True):
                            two_pointers += 1
                        if (object.binary_search == True):
                            binary_search += 1
                        if (object.dsu == True):
                            dsu += 1
                        if (object.strings == True):
                            strings += 1
                        if (object.number_theory == True):
                            number_theory += 1
                        if (object.data_structures == True):
                            data_structures += 1
                        if (object.hashing == True):
                            hashing += 1
                        if (object.shortest_paths == True):
                            shortest_paths += 1
                        if (object.matrices == True):
                            matrices += 1
                        if (object.string_suffix_structures == True):
                            string_suffix_structures += 1
                        if (object.dp == True):
                            dp += 1
                        if (object.greedy == True):
                            greedy += 1
                        if (object.graph_matchings == True):
                            graph_matchings += 1
                        if (object.games == True):
                            games += 1
                        if (object.schedules == True):
                            schedules += 1
                        if (object.dfs_and_similar == True):
                            dfs_and_similar += 1
                        if (object.meet_in_the_middle == True):
                            meet_in_the_middle += 1
                        if (object.constructive_algorithms == True):
                            constructive_algorithms += 1
                        if (object.bitmasks == True):
                            bitmasks += 1
                        if (object.flows == True):
                            flows += 1
                        if (object.divide_and_conquer == True):
                            divide_and_conquer += 1
                        if (object.geometry == True):
                            geometry += 1
                        if (object.math == True):
                            math += 1
                        if (object.sortings == True):
                            sortings += 1
                        if (object.ternary_search == True):
                            ternary_search += 1
                        if (object.combinatorics == True):
                            combinatorics += 1
                        if (object.implementation == True):
                            implementation += 1
                        if (object.brute_force == True):
                            brute_force += 1
                        if (object.sat_2 == True):
                            sat_2 += 1
                        if (object.trees == True):
                            trees += 1
                        if (object.probabilities == True):
                            probabilities += 1
                        if (object.graphs == True):
                            graphs += 1
                        if (object.chinese_remainder_theorem == True):
                            chinese_remainder_theorem += 1
                        if (object.interactive == True):
                            interactive += 1
                        if (object.other_tag == True):
                            other_tag += 1



                if (flag == 0):
                    prob_obj = Question(prob_link=ele)
                    try:
                        int(ele[-1])
                        prob_obj.prob_level = ele[-2]
                        type_list.append(ele[-2])
                    except:
                        prob_obj.prob_level = ele[-1]
                        type_list.append(ele[-1])
                    r4=requests.get(ele)
                    quessoup=BeautifulSoup(r4.text,"lxml")
                    tag=quessoup.find_all('span',attrs={'class':'tag-box'})
                    for ta in tag:
                        pt=ta.string.strip()
                        if(pt[0:1]=='*'):
                            if(pt[1:]=='special problem'):
                                prob_obj.special_problem=True
                                special_problem+=1
                            else:
                                prob_obj.prob_rat=int(pt[1:])
                                prob_rat.append(int(pt[1:]))
                        elif(pt=='expression parsing'):
                            prob_obj.expression_parsing=True
                            expression_parsing+=1
                        elif(pt=='fft'):
                            prob_obj.fft=True
                            fft+=1
                        elif(pt=='two pointers'):
                            prob_obj.two_pointers=True
                            two_pointers+=1
                        elif(pt=='binary search'):
                            prob_obj.binary_search=True
                            binary_search+=1
                        elif(pt=='dsu'):
                            prob_obj.dsu=True
                            dsu+=1
                        elif(pt=='strings'):
                            prob_obj.strings=True
                            strings+=1
                        elif(pt=='number theory'):
                            prob_obj.number_theory=True
                            number_theory+=1
                        elif(pt=='data structures'):
                            prob_obj.data_structures=True
                            data_structures+=1
                        elif(pt=='hashing'):
                            prob_obj.hashing=True
                            hashing+=1
                        elif(pt=='shortest paths'):
                            prob_obj.shortest_paths=True
                            shortest_paths+=1
                        elif(pt=='matrices'):
                            prob_obj.matrices=True
                            matrices+=1
                        elif(pt=='string suffix structures'):
                            prob_obj.string_suffix_structures=True
                            string_suffix_structures+=1
                        elif(pt=='interactive'):
                            prob_obj.interactive=True
                            interactive+=1
                        elif(pt=='chinese remainder theorem'):
                            prob_obj.chinese_remainder_theorem=True
                            chinese_remainder_theorem+=1
                        elif (pt == 'graphs'):
                            prob_obj.graphs=True
                            graphs+=1
                        elif (pt == 'probabilities'):
                            prob_obj.probabilities=True
                            probabilities+=1
                        elif (pt == 'trees'):
                            prob_obj.trees=True
                            trees+=1
                        elif (pt == '2-sat'):
                            prob_obj.sat_2=True
                            sat_2+=1
                        elif (pt == 'implementation'):
                            prob_obj.implementation=True
                            implementation+=1
                        elif (pt == 'brute force'):
                            prob_obj.brute_force =True
                            brute_force+=1
                        elif (pt == 'combinatorics'):
                            prob_obj.combinatorics =True
                            combinatorics+=1
                        elif (pt == 'ternary search'):
                            prob_obj.ternary_search =True
                            ternary_search+=1
                        elif (pt == 'sortings'):
                            prob_obj.sortings =True
                            sortings+=1
                        elif (pt == 'math'):
                            prob_obj.math =True
                            math+=1
                        elif(pt == 'graph matchings'):
                            prob_obj.graph_matchings=True
                            graph_matchings+=1
                        elif(pt == 'dp'):
                            prob_obj.dp=True
                            dp+=1
                        elif(pt == 'dfs and similar'):
                            prob_obj.dfs_and_similar=True
                            dfs_and_similar+=1
                        elif(pt == 'meet-in-the-middle'):
                            prob_obj.meet_in_the_middle=True
                            meet_in_the_middle+=1
                        elif(pt == 'games'):
                            prob_obj.games=True
                            games+=1
                        elif(pt == 'schedules'):
                            prob_obj.schedules=True
                            schedules+=1
                        elif(pt == 'constructive algorithms'):
                            prob_obj.constructive_algorithms=True
                            constructive_algorithms+=1
                        elif(pt == 'greedy'):
                            prob_obj.greedy=True
                            greedy+=1
                        elif(pt == 'bitmasks'):
                            prob_obj.bitmasks=True
                            bitmasks+=1
                        elif(pt == 'divide and conquer'):
                            prob_obj.divide_and_conquer=True
                            divide_and_conquer+=1
                        elif(pt == 'flows'):
                            prob_obj.flows=True
                            flows+=1
                        elif(pt == 'geometry'):
                            prob_obj.geometry=True
                            geometry+=1
                        else:
                            prob_obj.other_tag=True
                            other_tag+=1
                    prob_obj.save()

        try:
            # contests scrapping
            contests_link = "https://codeforces.com/contests/with/" + str(username)
            contests_l = requests.get(contests_link)
            contests_soup = BeautifulSoup(contests_l.text, "lxml")
            bestrank = -1
            worstrank = 100000
            maxsolved = -1
            maxchange = -30000
            minchange = 100000
            contest_graph = {}  # for line graph of contest

            ranks_1 = contests_soup.find('div', attrs={'class': 'datatable'}).find('tbody').find_all('tr')
            if (len(ranks_1) == 0):
                print("No contests given")
            else:
                for rows in ranks_1:
                    rinfo = rows.find_all('td')
                    cno = rinfo[0].string
                    cname = rinfo[1].find('a').string.strip()
                    crank = rinfo[2].find('a').string.strip()
                    bestrank = max(bestrank, int(crank))
                    worstrank = min(worstrank, int(crank))
                    csolved = rinfo[3].find('a').string.strip()
                    maxsolved = max(maxsolved, int(csolved))
                    change = rinfo[4].find('span').string
                    maxchange = max(maxchange, int(change))
                    minchange = min(minchange, int(change))
                    newrating = rinfo[5].string.strip()
                    try:
                        promote = rinfo[6].find('div').find('span').string
                    except:
                        promote = ''
                    if (promote != ''):
                        print(promote, ' at contest ', cno)

                    print(cname)
                    for object in ContestDb.objects.all():
                        if (object.contest_name == cname):
                            contest_graph[object.date] = newrating
                            print(object.date, newrating)
                            break

                print("maximum change of user :", maxchange)
                print("minimum change of user :", minchange)
                print("max_ques_solved: ", maxsolved)
                print('maximum rank achived by user: ', worstrank)
                print('minimum rank achived by user: ', bestrank)
                print(contest_graph)
        except:
            pass

        print(verdict_list)
        print(tag_list)

        return exists, rank, color, ar, institute, rating, tag_list, prob_rat, type_list, lang_list, verdict_list

    except:
        exists = False
        return exists
