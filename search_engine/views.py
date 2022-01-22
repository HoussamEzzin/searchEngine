from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
from django.views.generic import View
from django.http import JsonResponse
import json
from .models import Article
from django.views.generic import ListView, DetailView


def home(request):
    
    context = {
            'articles': Article.objects.all()
        }
    
    return render(request, 'search_engine/home.html', context)


class ArticelDetailView(DetailView):
    template_name = 'search_engine/read.html'
    model = Article
    
class SearchEngineView(TemplateView):
    template_name = 'search_engine/home.html'
    
class SearchEngineApi(View):
    
    def post(self, request, *args, **kwargs):
        input_data = json.loads(request.body.decode('utf-8'))
        
        print('INPUT IS ', input_data)
        
        
        articles = Article.objects.all()
        
        input = input_data['text']
        found = []
        for article in articles:
            f = dict()
            if input in article.content:
                # found.append(article.id)
                f['author'] = article.author
                f['content'] = article.content
                f['keywords'] = article.keywords
                f['title'] = article.title
                f['id'] = article.id
                found.append(f)
            elif input in article.author:
                f['author'] = article.author
                f['content'] = article.content
                f['keywords'] = article.keywords
                f['title'] = article.title
                f['id'] = article.id
                found.append(f)
            elif input in article.keywords:
                f['author'] = article.author
                f['content'] = article.content
                f['keywords'] = article.keywords
                f['title'] = article.title
                f['id'] = article.id
                found.append(f)
            elif input in article.title:
                f['author'] = article.author
                f['content'] = article.content
                f['keywords'] = article.keywords
                f['title'] = article.title
                f['id'] = article.id
                found.append(f)
                
        
        
        
        
        
        response_data = {
            'result': found
            }
        return JsonResponse(response_data,status=200)