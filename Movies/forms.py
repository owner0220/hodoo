from django import forms
from .models import Genre, Movie, Score

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        
        
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        
        
class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['content', 'score']
    
    
    
