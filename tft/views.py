from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))