from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("전략적 팀 전투 웹 크롤링")