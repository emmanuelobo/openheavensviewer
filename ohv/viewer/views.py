from django.shortcuts import render
from django.http import request


def home(request): # show devotional for today by default
	return render(request, "index.html")

def devotional(): # actual devotional reading
	pass
