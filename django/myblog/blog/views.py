from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models

def index(request):
    articles = models.article.objects.all()
    return render(request, "blog/index.html",{'articlex':articles})

def article_page(request,article_id):
    article = models.article.objects.get(pk=article_id)
    return render(request,"blog/article_page.html",{"article":article})

def edit_page(request,article_id):
    if str(article_id)== '0':
        return render(request,'blog/Edit_page.html')
    article=models.article.objects.get(pk=article_id)
    return render(request,'blog/Edit_page.html',{'article':article})

def edit_action(request):
    title=request.POST.get('title','TITLE')
    content=request.POST.get('content','CONTENT')
    article_id=request.POST.get('article_id','0')
    if(article_id=='0'):
        models.article.objects.create(title=title,content=content)
        articles=models.article.objects.all()
        return HttpResponseRedirect('/blog/index')
    article=models.article.objects.get(pk=article_id)
    article.title=title
    article.content=content
    article.save()
    return render(request,"blog/article_page.html",{"article":article})
# Create your views here.
