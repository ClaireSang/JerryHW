from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import User
# Create your views here.
def index(request):
	users = User.objects.all()
	return render_to_response('person/profiles.html',locals())