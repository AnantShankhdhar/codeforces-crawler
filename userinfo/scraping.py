from . import models

def scrape(username):
    import requests
    exists = True
    try:    
        profile="https://codeforces.com/profile/"+str(username)
        sub="https://codeforces.com/submissions/"+str(username)
        r1=requests.get(profile)
        r2=requests.get(sub)
        from bs4 import BeautifulSoup
        profilesoup= BeautifulSoup(r1.text,"lxml")
        subsoup= BeautifulSoup(r2.text,"lxml")
        info=profilesoup.find('div',attrs={'class':'info'})
        maininfo=info.find('div',attrs={'class':'main-info'})
        userrank=maininfo.find('div',attrs={'class':'user-rank'})  #fine
        rank=userrank.find('span').string #Rank

        color=userrank.find('span').get('class')
        for c in color:
            color=c[5:]    #Color
        ar = ''
        try:    
            details=maininfo.find('div',attrs={'style':'margin-top: 0.5em;'})   #problem
            detail=details.find('div',attrs={'style':'font-size: 0.8em; color: #777;'})
            for child in detail.children:
                ar=ar+(child.string)
        except:
            ar += "No info"
        try:    
            detail1=detail.find_next_sibling()
            institute=detail1.find('a').string #institute
        except:
            institute = "Institute not mentioned"
        try:
            rating=info.find('ul').find('li').find('span').string #rating
        except:
            rating = "Not given any contest"

        try:    
            pg=subsoup.find_all('div',attrs={'class':'pagination'})[1].find('ul').find_all('li')[-2].find('a').string  #pages
        except:
            pg=1
        ac=0
        wa=0
        tle=0
        rte=0
        mle=0
        challenged=0
        cpe=0
        skipped=0
        ile=0
        other=0
        
        #Problem tags
        expression_parsing=0
        fft=0
        two_pointers=0
        binary_search=0
        dsu=0
        strings=0
        number_theory=0
        data_structures=0
        hashing=0
        shortest_paths=0
        matrices=0
        string_suffix_structures=0
        graph_matchings=0
        dp=0
        dfs_and_similar=0
        meet_in_the_middle=0
        games=0
        schedules=0
        constructive_algorithms=0
        greedy=0
        bitmasks=0
        divide_and_conquer=0
        flows=0
        geometry=0
        math=0
        sortings=0
        ternary_search=0
        combinatorics=0
        brute_force=0
        implementation=0
        sat_2=0
        trees=0
        probabilities=0
        graphs=0
        chinese_remainder_theorem=0
        interactive=0
        other_tag=0
        special_problem=0
        prob_rat=[]
        link_list=[]
        type_list=[]
        lang_list=[]
        
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
                            special_problem++
                        #elif()


                if (flag == 0):
                    prob_obj = Question.objects.create(prob_link=ele)
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
                                special_problem++
                            else:
                                prob_obj.prob_rat=pt[1:]
                                prob_rat.append(pt[1:])
                        elif(pt=='expression parsing'):
                            prob_obj.expression_parsing=True
                            expression_parsing++
                        elif(pt=='fft'):
                            prob_obj.fft=True
                            fft++
                        elif(pt=='two pointers'):
                            prob_obj.two_pointers=True
                            two_pointers++
                        elif(pt=='binary search'):
                            prob_obj.binary_search=True
                            binary_search++
                        elif(pt=='dsu'):
                            prob_obj.dsu=True
                            dsu++
                        elif(pt=='strings'):
                            prob_obj.strings=True
                            strings++
                        elif(pt=='number theory'):
                            prob_obj.number_theory=True
                            number_theory++
                        elif(pt=='data structures'):
                            prob_obj.data_structures=True
                            data_structures++
                        elif(pt=='hashing'):
                            prob_obj.hashing=True
                            hashing++
                        elif(pt=='shortest paths'):
                            prob_obj.shortest_paths=True
                            shortest_paths++
                        elif(pt=='matrices'):
                            prob_obj.matrices=True
                            matrices++
                        elif(pt=='string suffix structures'):
                            prob_obj.string_suffix_structures=True
                            string_suffix_structures++
                        elif(pt=='interactive'):
                            prob_obj.interactive=True
                            interactive++
                        elif(pt=='chinese remainder theorem'):
                            prob_obj.chinese_remainder_theorem=True
                            chinese_remainder_theorem++
                        elif (pt == 'graphs'):
                            prob_obj.graphs=True
                            graphs++
                        elif (pt == 'probabilities'):
                            prob_obj.probabilities=True
                            probabilities++
                        elif (pt == 'trees'):
                            prob_obj.trees=True
                            trees++
                        elif (pt == '2-sat'):
                            prob_obj.sat_2=True
                            sat_2++
                        elif (pt == 'implementation'):
                            prob_obj.implementation=True
                            implementation++
                        elif (pt == 'brute force'):
                            prob_obj.brute_force =True
                            brute_force++
                        elif (pt == 'combinatorics'):
                            prob_obj.combinatorics =True
                            combinatorics++
                        elif (pt == 'ternary search'):
                            prob_obj.ternary_search =True
                            ternary_search++
                        elif (pt == 'sortings'):
                            prob_obj.sortings =True
                            sortings++
                        elif (pt == 'math'):
                            prob_obj.math =True
                            math++
                        elif(pt == 'graph matchings'):
                            prob_obj.graph_matchings=True
                            graph_matchings++
                        elif(pt == 'dp'):
                            prob_obj.dp=True
                            dp++
                        elif(pt == 'dfs and similar'):
                            prob_obj.dfs_and_similar=True
                            dfs_and_similar++
                        elif(pt == 'meet-in-the-middle'):
                            prob_obj.meet_in_the_middle=True
                            meet_in_the_middle++
                        elif(pt == 'games'):
                            prob_obj.games=True
                            games++
                        elif(pt == 'schedules'):
                            prob_obj.schedules=True
                            schedules++
                        elif(pt == 'constructive algorithms'):
                            prob_obj.constructive_algorithms=True
                            constructive_algorithms++
                        elif(pt == 'greedy'):
                            prob_obj.greedy=True
                            greedy++
                        elif(pt == 'bitmasks'):
                            prob_obj.bitmasks=True
                            bitmasks++
                        elif(pt == 'divide and conquer'):
                            prob_obj.divide_and_conquer=True
                            divide_and_conquer++
                        elif(pt == 'flows'):
                            prob_obj.flows=True
                            flows++
                        elif(pt == 'geometry'):
                            prob_obj.geometry=True
                            geometry++
                        else:
                            prob_obj.other_tag=True
                            other_tag++
        except:
            pass

        print('expression_parsing',expression_parsing)
        print("fft",fft)
        print("two_pointers",two_pointers)
        print('binary_search',binary_search)
        print("dsu",dsu)
        print("strings",strings)
        print('number_theory',number_theory)
        print('data_structures',data_structures)
        print('hashing',hashing)
        print('shortest_paths',shortest_paths)
        print('matrices',matrices)
        print('string_suffix_structures',string_suffix_structures)
        print('graph_matchings',graph_matchings)
        print('dp',dp)
        print('dfs_and_similar',dfs_and_similar)
        print('meet-in-the-middle',meet_in_the_middle)
        print('games',games)
        print('schedules',schedules)
        print('constructive_algorithms',constructive_algorithms)
        print('greedy',greedy)
        print('bitmasks',bitmasks)
        print('divide_and_conquer',divide_and_conquer)
        print('flows',flows)
        print('geometry',geometry)
        print('math',math)
        print('sortings',sortings)
        print('ternary_search',ternary_search)
        print('combinatorics',combinatorics)
        print('brute_force',brute_force)
        print('implementation',implementation)
        print('2-sat',sat_2)
        print('trees',trees)
        print('probabilities',probabilities)
        print('graphs',graphs)
        print('chinese_remainder_theorem',chinese_remainder_theorem)
        print('interactive',interactive)
        print('Special problem',special_problem)
        print(prob_rat)
        print(type_list)
        print(lang_list)
        return exists,rank,color,ar,institute,ac,wa,tle,rte,mle,challenged,cpe,skipped,ile,other,rating
    except:
        exists = False
        return exists
