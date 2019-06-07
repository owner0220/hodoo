from bs4 import *
import requests
import json

def testing(day):
    req = requests.get("https://movie.naver.com/movie/running/premovie.nhn")
    respon = req.text
    # print(req)
    soup = BeautifulSoup(respon, 'html.parser')
    # print(type(soup))
    
    # print(soup.find_all(class_="obj_section"))
    obj_section = soup.find(class_="obj_section") 
    days = obj_section.find_all(class_="lst_wrap")
    dayandsrc=dict()
    for day in days[day*2:(day+1)*2:1]:
        date = day.find_all('strong')
    
        key = ""
        for dt in date:
            tmp = dt.find_all('span')
            sss=list()
            ct = 0 
            tmp2 = ""
            for tp in tmp[1::1]:
                tt = tp.find(class_='blind')
                if tt!=None:
                    ct+=1
                    tmp2 += tt.contents[0]
                    if ct == 10:
                        ct = 0
    
            # 일자가 저장된다.
            key=tmp2
        items = day.find_all('li')
        
        c=0     
        tmp3=dict()
        for item in items:
            c+=1
            tmp4=list()
            movie_poster=item.find('img').get('src')
            movie_poster=movie_poster.split("?")[0]+"type=m203_290_2"
            rate=item.find('span').string.split()[0]
            print(rate)
            href=item.find('a').get('href')
            tmp4.append(movie_poster)
            tmp4.append(href)
            tmp4.append(rate)
            # print(href)
            movie_name=item.find('img').get("alt")
            tmp3[movie_name]=tmp4
        # print(tmp3)
        dayandsrc[key]=tmp3

    # print(dayandsrc)
    return dayandsrc
