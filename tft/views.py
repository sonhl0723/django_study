from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json

# selenium 불러오기
# import os
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManagr

# URL="https://www.gopax.co.kr/exchange/btc-krw"

# def index(self):
#     driver = webdriver.Chrome(ChromeDriverManagr.install())
#     driver.implicitly_wait(10)

#     driver.get(URL)
    
#     bitcoin_price = driver.get.find_element_by_class_name('TradingPair__currentPriceValue')
#     print(bitcoin_price.text)
#     # return HttpResponse(bitcoin_price)

def index(request):
    return render(request, 'index.html')

def search_result(request):
    if request.method == "GET":
        # api_key / params 설정
        api_key = 'RGAPI-d6f8cd1e-c35b-48e1-99e0-d455318676da'
        params = {'api_key': api_key}

        # summonerName 검색으로 encryptedSummonerId 얻기
        summonerName = request.GET.get('search_name')
        summoner_url = "https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/" + str(summonerName)
        res = requests.get(summoner_url, headers={"X-Riot-Token": api_key})
        summoner_exist = False
        summoner_result = {}
        if res.status_code == requests.codes.ok:
            summoner_exist = True
            summoner_result = res.json()
            # summoner_result = json.loads(res.text)
            # summoners_result = json.loads(((res.text).encode('utf-8')))
            summoner_Id = summoner_result['id']

            # encryptedSummonerId로 전적 로드
            leage_url = "https://kr.api.riotgames.com/tft/league/v1/entries/by-summoner/" + str(summoner_Id)
            res_leage = requests.get(leage_url, headers={"X-Riot-Token": api_key})
            leage_result = {}
            leage_result = res_leage.json()
            user_result = {}
            leage_result = leage_result.pop()
            user_result['rank'] = leage_result['rank']
            user_result['leaguePoints'] = leage_result['leaguePoints']
            user_result['wins'] = leage_result['wins']
            user_result['losses'] = leage_result['losses']
            user_result['tier'] = leage_result['tier']
            
    return render(request, 'search_result.html', {'summoner_exist': summoner_exist, 'user_result': user_result})
    # return print(json.loads(res.text)