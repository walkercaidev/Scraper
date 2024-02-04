Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> requests.get('https://online.carrefour.com.tw/zh/%E7%B5%B1%E4%B8%80%E9%99%BD%E5%85%89/1501401100101.html')
<Response [200]>
>>> res = requests.get('https://online.carrefour.com.tw/zh/%E7%B5%B1%E4%B8%80%E9%99%BD%E5%85%89/1501401100101.html')
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(res.text,'html.parser')
>>> tag_name = 'span.money'
>>> span_money = soup.select(tag_name)
>>> soya_milk_price = span_money[0].text.strip()
>>> soya_milk_price
'17'
