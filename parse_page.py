from bs4 import BeautifulSoup

def parse_page(page):
    soup = BeautifulSoup(page, 'html.parser')
    courses = []
    table = soup.find('table', {'class': 'data'}).find('tbody').children
    for row in table:
        if str(row) != '\n':
            soup = BeautifulSoup(str(row), 'html.parser')
            data = soup.find('tr').findAll('td')
            data = [str(entry).replace('<td>', '').replace('</td>', '') for entry in data]
            courses.append(data)
    return courses