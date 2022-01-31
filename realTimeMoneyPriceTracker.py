# -*- coding: utf-8 -*-
"""
@author: IdrisIbrahimERTEN
"""

import requests
from bs4 import BeautifulSoup
import time

# paranın fiyatını almak için bir fonksiyon yarat

def get_latest_money_price(money):
    url = 'https://www.google.com/search?q=' + (money)
    # make a request to the website
    HTML = requests.get(url)
    # Parsse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser')
    # find the current price
    texti = soup.find('div', attrs={
        'class': 'BNeawe iBp4i AP7Wnd'
    }).find({
        'div': 'BNeawe iBp4i AP7Wnd'
    }).text
    return texti


price = get_latest_money_price('1euro')
print('Euro price : ' + price)
price = get_latest_money_price('dollar')
print('Dolar price : ' + price)

