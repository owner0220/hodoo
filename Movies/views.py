from django.shortcuts import render, redirect
from .forms import MovieForm, ScoreForm, GenreForm
from .models import Movie, Score, Genre
from django.http import HttpResponse
from .crawling import *
from .movie_update import *
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'movies/main.html')


def list(request):
    if request.GET.get('page'):
        page = request.GET.get('page')
        page = int(page)
        if page != 1:
            movies = Movie.objects.all()[(page-1)*9:page*9-1:1]
            pages = [page-1,page,page+1]
        else:
            movies = Movie.objects.all()[(page-1)*9:page*9-1:1]
            pages = [1,2,3]
    else:
        page = 1
        movies = Movie.objects.all()[(page-1)*9:page*9-1:1]
        pages = [1,2,3]
    # raise("wqeqwe")    
    return render(request, 'movies/list.html', {'movies':movies,'pages':pages})



def detail(request, id):
    movie = Movie.objects.get(id=id)
    score_form = ScoreForm()
    likes = movie.likes
    score_sum = 0
    for sc in movie.score_set.all():
        score_sum += sc.score
    if score_sum == 0:
        score_avg = 0
    else:
        
        score_avg = score_sum/movie.score_set.all().count()
        score_avg = round(score_avg,2)
        
    
    print(likes)
    return render(request,'movies/detail.html',{'movie':movie, 'score_form':score_form, 'likes':likes, 'score_avg':score_avg})
    

@permission_required('movies')
def delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('movies:list')


@permission_required('movies')    
def update(request, id):
    movie = Movie.objects.get(id=id)
    if(request.method == "POST"):
        form = MovieForm(request.POST, instance=movie)
        if(form.is_valid()):
            form.save()
            return redirect("movies:list")
    else:
        form = MovieForm(instance=movie)
    
    return render(request, 'movies/form.html', {"form":form})   

@permission_required('movies')
def create(request):
    # 1. get 방식으로 데이터를 입력할 form을 요청한다.
    # 4. 사용자가 데이터를 입력해서 post방식으로 요청한다.
    # 9. 사용자가 다시 적절한 데이터를 입력해서 post방식으로 요청한다.
    if request.method == "POST":
        # 5. post방식으로 저장요청을 받고, 데이터를 받아 PostForm에 넣어서 인스턴스화 한다.
        # 10. 5번과 같음
        form = MovieForm(request.POST) # 사진을 받기 위해 request.FILES도 추가
        # 6. 데이터 검증을 한다.
        # 11. 6번과 같음 
        if form.is_valid():
            # 12. 적절한 데이터가 들어온다. 데이터를 저장하고 list페이지로 리다이렉트
            movie = form.save(commit=False)
            movie.save()
            return redirect('movies:detail', movie.id)
    else :
        # 2. PostForm을 인스턴스화 시켜서 form에 저장한다.
        form = MovieForm()
    # 3. form을 담아서 create.html을 보내준다.
    # 8. 사용자가 입력한 데이터는 form에 담아진 상태로 다시 form을 담아서 create.html을 보내준다.
    return render(request,'movies/form.html',{'form':form})
    

@login_required
def score_new(request,id):
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        score_form = ScoreForm(request.POST)
        print("저장됨?????")
        print(score_form)
        if score_form.is_valid():
            print("=======================")
            score = score_form.save(commit=False)
            score.movie_id = Movie.objects.get(id=id)
            score.current_user = request.user
            score.save()
            print("저장됨")
        return redirect("movies:detail", id)
            

@login_required           
def score_delete(request, id, score_new_id):
    new = Score.objects.get(id=score_new_id)
    new.delete()
    return redirect('movies:detail', id)

@login_required
def score_update(request, id, score_id):
    score = Score.objects.get(id=score_id)
    if(request.method == "POST"):
        form = ScoreForm(request.POST, instance=score)
        if(form.is_valid()):
            form.save()
            return redirect("movies:detail",id)
    else:
        form = ScoreForm(instance=score)
    
    return render(request, 'movies/form.html', {"form":form})  


    
def preticket(request):
    if request.GET.get('day'):
        day = request.GET.get('day')
        day = int(day)
        print(day)
        if day != 0:
            items = testing(day-1)
            days = [day-1,day,day+1]
        else:
            items = testing(0)
            days = [1,2,3]
    else:
        items = testing(0)
        days = [1,2,3]
    return render(request,"movies/preticket.html",{"items":items,"days":days})
    
    
    
    
    
    

@login_required
def like(require, id):
    user = require.user
    movie = Movie.objects.get(id=id)
    #사용자가 좋아요를 눌렀다면
    if user in movie.likes.all():
        movie.likes.remove(user)
    #사용자가 좋아요를 누르지 않았다면
    else:
        movie.likes.add(user)

    return redirect('movies:detail', id)
    
@login_required
def watched(require, id):
    user = require.user
    movie = Movie.objects.get(id=id)
    #사용자가 좋아요를 눌렀다면
    if user in movie.watch.all():
        movie.watch.remove(user)
    #사용자가 좋아요를 누르지 않았다면
    else:
        movie.watch.add(user)

    return redirect('movies:detail', id)
    

@login_required
def like_post(request):
    movies = (request.user.like_movie_set.all())
    return render(request, 'movies/like_post.html', {'movies':movies})
    

@login_required
def watched_post(request):
    movies = (request.user.watched.all())
    return render(request, 'movies/watched_post.html', {'movies':movies})


@permission_required('movies')
def put_data(request,year):
    print("실행중")
    past_year_update(int(year))
    print("실행완료")
    return HttpResponse("완료")
    
@login_required
def search(request):
    qs = Movie.objects.all()

    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        qs = qs.filter(title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
    return render(request, 'movies/search.html', {
        'search' : qs,
        'q' : q,
    })