from django.shortcuts import render_to_response
from django.http import HttpResponse

from django.http import HttpResponseRedirect

from . models import Message
from . import models
import datetime


# Create your views here.
def home(request):
	return HttpResponse("Mom! Look here!")


def index(request):
	mg = Message.objects.all()
	return render_to_response('mothers_day/index.html',locals())


def save(request):
	username = request.POST.get("username")
	title = request.POST.get("title")
	content = request.POST.get("content")
	publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	message = models.Message(title = title, content = content, username = username, publish = publish)
	message.save()

	return HttpResponseRedirect('/mothers_day/')