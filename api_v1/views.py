from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from webapp.models import Article
# Create your views here.


def echo_view(request, *args, **kwargs):
    print(request.body)
    print(json.loads(request.body))
    response_data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method
    }
    if request.body:
        response_data['content'] = json.loads(request.body)
    response_data_json = json.dumps(response_data)
    response = HttpResponse(response_data_json)
    response['Content-Type'] = 'application/json'
    return response


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):

    if request.method == 'GET':
        return HttpResponse()

    return HttpResponseNotAllowed('Only GET request are allowed')

def article_view(request, *arg, **kwargs):
    if request.method == 'GET':
        article_data = []
        # for article in Article.objects.all():
        #     article_data.append({
        #         'title': article.title,
        #         'content':  article.content
        #     })
        article_data = list(Article.objects.values('title', 'content'))
        return JsonResponse(article_data, safe=False)
    elif request.method == "POST":
        request_data = json.loads(request.body)
        print(request_data)
        artticle = Article.objects.create(**request_data)
        return  JsonResponse({'id': artticle.pk})
    return HttpResponseNotAllowed('Only GET request are allowed')