from django.shortcuts import render, redirect
from .forms import MovieForm, ScoreForm, GenreForm
from .models import Movie, Score, Genre


# Create your views here.

def list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html', {'movies':movies})

def detail(request, id):
    movies = Movie.objects.get(id=id)
    score_form = ScoreForm()
    return render(request,'movies/detail.html',{'movies':movies, 'score_form':score_form})
    
def delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('movies:list')
    
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
    


def score_new(request,id):
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        score_form = ScoreForm(request.POST)
        if score_form.is_valid():
            score = score_form.save(commit=False)
            score.movie_id = Movie.objects.get(id=id)
            score.save()
            return redirect("movies:detail", id)
            
            
def score_delete(request, id, score_new_id):
    new = Score.objects.get(id=score_new_id)
    new.delete()
    return redirect('movies:detail', id)