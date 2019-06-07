# from urllib.request import Request,urlopen
from datetime import date, timedelta
from .models import Movie
import requests
import json
import os



def find_year_sundays(year):
    dt = date(year,12,28)
    if year == date.today().year:
        dt = date.today() - timedelta(days=7)
    
    print(dt.day)
    dt += timedelta(days = 6-dt.weekday())
    print(dt.day)
    print(dt.month)

    while dt.year >= year and dt<date.today():
        yield dt
        dt -= timedelta(days = 7)
            



def get_req_json(url,headers={}):
    res = requests.get(url,headers=headers)
    result = res.text
    json_result = json.loads(result)
    return json_result           


    # 파이썬 기본 라이브러리 url에서 한글로 검색하는게 안됨 ㅡㅡ
    # req = Request(url,method="GET",headers=headers)
    #스트림을 열어서 결과를 읽어 나온 str 정보를 result에 저장한다.
    # with urlopen(req) as f:
    #     result = (f.read().decode('utf-8'))
    #     # print(result)
        # print(type(result))
    #저장된 str을 객체로 변환해준다.
    #str의 포맷이 json 규칙이기 때문에 json parse를 이용해
    #객체로 변환해 준다.
    # print(json_result)


def movie_update(json_object):
    movieList = json_object.get("boxOfficeResult").get("weeklyBoxOfficeList")
    for movie in movieList:
        title = movie.get('movieNm')
        audi = movie.get('audiAcc')
        
        
        naver = "https://openapi.naver.com/v1/search/movie.json?query="+title
        nMovie = get_req_json(naver,headers={"X-Naver-Client-Id":os.environ['nc'],"X-Naver-Client-Secret":os.environ['ns']}).get("items")
        nPoster = "f"
        if len(nMovie)!=0:
            nMovie=nMovie[0]
            nPoster = nMovie.get('image')


        theMvDB = "https://api.themoviedb.org/3/search/movie?api_key="+os.environ['db']+"&query="+title+"&language=ko-kr"
        MvDB = get_req_json(theMvDB).get("results")
        DBPoster = "f"
        summary = "f"
        poster_back = "f"
        release_date=""
        if len(MvDB)!=0:
            MvDB = MvDB[0]
            pospath=MvDB.get('poster_path')
            if pospath != None:
                DBPoster = "https://image.tmdb.org/t/p/w500"+MvDB.get('poster_path')
                if MvDB.get('backdrop_path'):
                    poster_back = "https://image.tmdb.org/t/p/original"+MvDB.get('backdrop_path')
                else:
                    poster_back = "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"
                
            summary = MvDB.get('overview')
            release_date=MvDB.get('release_date')
        
        poster_url="f"
        if DBPoster =="f":
            poster_url = nPoster
        else:
            poster_url = DBPoster
        
        try:
            Movie.objects.get(title=title)
        except:
            Movie(title = title,overview=summary,poster_path=poster_url,poster_back=poster_back).save()
        
        print(title)
        print(audi)
        print(summary)
        print(poster_url)
        print(poster_back)
        
        
        
        
def past_year_update(year):
    if year <= date.today().year:
        for s in find_year_sundays(year):
            korean = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key="+os.environ['kk']+"&targetDt=" + "".join(str(s).split('-'))
            print(s,"=============")
            movie_update(get_req_json(korean))
        return True
    else:
        return False
        

    
