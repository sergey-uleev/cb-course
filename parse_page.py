from bs4 import BeautifulSoup

def parse_page(page):
    soup = BeautifulSoup(page)
    courses = soup.find('table', {'class': 'data'})
    return courses