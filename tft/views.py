from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json
# selenium 모듈
from selenium import webdriver
# riot api 키 복사 후 붙여넣기 기능 모듈
import pyperclip
import os

def login(request):
    return render(request, 'login.html')

def search(request):

    user_id = request.POST.get('user_id')
    user_pwd = request.POST.get('user_pwd')

    user_info = {
        'id' : user_id,
        'pwd' : user_pwd
    }

    return render(request, 'search.html', {'user_info':user_info})

def search_result(request):
    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    # 새로운 chrome 창 안뜨게 설정
    driver_options = webdriver.ChromeOptions()
    driver_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # driver_options.add_argument('headless') # 새로운 창 사용 중지
    driver_options.add_argument("--disable-dev-shm-usage")
    driver_options.add_argument("--no-sandbox")
    driver_options.add_argument('lang=ko_KR') # 언어 설정

    # riot developer 접속
    # driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=driver_options) 
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=driver_options)
    driver.get("https://developer.riotgames.com/")

    # LOGIN 버튼 클릭
    driver.find_element_by_css_selector(".navbar-avatar").click()

    # riot 아이디 / 비밀번호 입력 후 로그인 버튼 클릭
    driver.implicitly_wait(5)
    admin_id = driver.find_element_by_name("username")
    admin_pwd = driver.find_element_by_name("password")
    admin_id.send_keys(request.POST.get('user_id'))
    admin_pwd.send_keys(request.POST.get('user_pwd'))
    driver.find_element_by_css_selector(".mobile-button").click()

    driver.implicitly_wait(5)
    driver.find_element_by_id("apikey_copy").click()
    driver.implicitly_wait(1)

    if request.method == "POST":
        api_key = pyperclip.paste()

        # summonerName 검색으로 encryptedSummonerId 얻기
        summonerName = request.POST.get('search_name')
        summoner_url = "https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/" + str(summonerName)
        res = requests.get(summoner_url, headers={"X-Riot-Token": api_key})
        summoner_exist = False
        summoner_result = {}
        user_result = {}

        user_id = request.POST.get('user_id')
        user_pwd = request.POST.get('user_pwd')
        user_info = {
            'user_id' : user_id,
            'user_pwd' : user_pwd
        }
        
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
            leage_result = leage_result.pop()
            user_result['rank'] = leage_result['rank']
            user_result['leaguePoints'] = leage_result['leaguePoints']
            user_result['wins'] = leage_result['wins']
            user_result['losses'] = leage_result['losses']
            user_result['tier'] = leage_result['tier']
            
    return render(request, 'search_result.html', {'summoner_exist': summoner_exist, 'user_result': user_result, 'user_info': user_info})