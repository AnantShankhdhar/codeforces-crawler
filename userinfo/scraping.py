def scrape(username):
    import requests
    #username=input()
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
        
        #print(rank) 
        color=userrank.find('span').get('class')
        for c in color:
            color=c[5:]    #Color
        print(color)
        ar = ''
        try:    
            details=maininfo.find('div',attrs={'style':'margin-top: 0.5em;'})   #problem
            detail=details.find('div',attrs={'style':'font-size: 0.8em; color: #777;'})
            #ar=''
            for child in detail.children:
                ar=ar+(child.string)
            #print(ar)  #basic info    
        except:
            ar += "No info"
            #print("No info")   
        try:    
            detail1=detail.find_next_sibling()
            institute=detail1.find('a').string #institute
            print(institute)
        except:
            institute = "Not mentioned"
            #print("Not mentioned") 
        try:
            rating=info.find('ul').find('li').find('span').string #rating
            #print(rating)
        except:
            rating = "Not given any contest"
            print("Not given any contest")

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
                    print(i)
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
                #lang_list.append(lang)
                if(pr!=None):
                    ques=pro.find_all('a')[-1]
                    ql=ques.get('href')
                    qlink='https://codeforces.com'+str(ql)
                    link_list.append(qlink)
                    new_l=set(link_list)
                    new_list=list(new_l)
                    
        for ele in new_list:
            try:
                int(ele[-1])
                type_list.append(ele[-2])
            except:    
                type_list.append(ele[-1])
            r4=requests.get(ele)
            quessoup=BeautifulSoup(r4.text,"lxml")
            tag=quessoup.find_all('span',attrs={'class':'tag-box'})
            for ta in tag:
                pt=ta.string.strip()
                if(pt[0:1]=='*'):
                    if(pt[1:]=='special problem'):
                        special_problem+=1
                    else:    
                        prob_rat.append(pt[1:])
                elif(pt=='expression parsing'):
                    expression_parsing+=1
                elif(pt=='fft'):
                    fft+=1
                elif(pt=='two pointers'):
                    two_pointers+=1
                elif(pt=='binary search'):
                    binary_search+=1
                elif(pt=='dsu'):
                    dsu+=1
                elif(pt=='strings'):
                    strings+=1
                elif(pt=='number theory'):
                    number_theory+=1
                elif(pt=='data structures'):
                    data_structures+=1
                elif(pt=='hashing'):
                    hashing+=1
                elif(pt=='shortest paths'):
                    shortest_paths+=1
                elif(pt=='matrices'):
                    matrices+=1
                elif(pt=='string suffix structures'):
                    string_suffix_structures+=1
                elif(pt=='interactive'):
                    interactive=interactive+1
                elif(pt=='chinese remainder theorem'):
                    chinese_remainder_theorem=chinese_remainder_theorem+1
                elif (pt == 'graphs'):
                    graphs = graphs + 1
                elif (pt == 'probabilities'):
                    probabilities = probabilities + 1
                elif (pt == 'trees'):
                    trees = trees + 1
                elif (pt == '2-sat'):
                    sat_2 = sat_2 + 1
                elif (pt == 'implementation'):
                    implementation = implementation + 1
                elif (pt == 'brute force'):
                    brute_force = brute_force + 1
                elif (pt == 'combinatorics'):
                    combinatorics = combinatorics + 1
                elif (pt == 'ternary search'):
                    ternary_search = ternary_search + 1
                elif (pt == 'sortings'):
                    sortings = sortings + 1
                elif (pt == 'math'):
                    math = math+ 1 
                elif(pt == 'graph matchings'):
                    graph_matchings+= 1
                elif(pt == 'dp'):
                    dp+= 1
                elif(pt == 'dfs and similar'):
                    dfs_and_similar+=1
                elif(pt == 'meet-in-the-middle'):
                    meet_in_the_middle+=1
                elif(pt == 'games'):
                    games+=1
                elif(pt == 'schedules'):
                    schedules+=1
                elif(pt == 'constructive algorithms'):
                    constructive_algorithms+=1
                elif(pt == 'greedy'):
                    greedy+=1
                elif(pt == 'bitmasks'):
                    bitmasks+=1
                elif(pt == 'divide and conquer'):
                    divide_and_conquer+=1
                elif(pt == 'flows'):
                    flows+=1
                elif(pt == 'geometry'):
                    geometry+=1
                else:
                    other_tag+=1    
                            
        print('ac=',ac)
        print('wa=',wa)
        print('tle=',tle)
        print('rte=',rte)
        print('mle=',mle)
        print('challenged=',challenged)
        print('cpe',cpe)
        print('skipped=',skipped)
        print('ile=',ile)
        print('other=',other)
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
        return rank,color,ar,institute,ac,wa,tle,rte,mle,challenged,cpe,skipped,ile,other,rating
    except:
        s = "No such username"
        return s
        #print("No such username")