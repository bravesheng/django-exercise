from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    s = "Hello World!"
    return HttpResponse(s)

from article.models import Article
from django.shortcuts import render

def detail(request, pk):
    article = Article.objects.get(pk=int(pk))
    return render(request, "detail.html", {'article': article})

from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', ]

from django.http import HttpResponseRedirect

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save()
            return HttpResponseRedirect('/article/' + str(new_article.pk))

    form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

from django.http import Http404

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)