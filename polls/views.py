from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from .models import Votes


def index(request):
    html = loader.get_template('search.html')
    votes = Votes.objects.all().values()
    content = {'votes': votes, 'post': request.POST}
    request.session['name'] = 'Von Wilhelm Guiang'
    return HttpResponse(html.render(content, request))


@csrf_protect
def search(request):
    name = request.POST['name_field']
    name_search = Votes.objects.filter(first_name__contains=name).values()
    cont = {'results': name_search}
    return render(request,'search.html', cont)
