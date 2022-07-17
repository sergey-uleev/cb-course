from get_page import *
from parse_page import *

if __name__ == '__main__':
    date = input('Введите дату: ')
    cur = input('Введите буквенный код валюты: ').upper()
    page = get_page(date)
    courses = parse_page(page)
    for course in courses:
        if course[1] == cur:
            print(course)
            break
    
        
