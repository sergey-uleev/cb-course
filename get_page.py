import requests

def get_page(date):
    url = 'https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To=' + date
    r = requests.get(url)
    return r.text 