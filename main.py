from get_page import *
from parse_page import *
from format_str import *
from utils import *

if __name__ == '__main__':
    date = input('Введите дату: ')
    if not_in_future(date):
        cur = input('Введите буквенные коды валют через пробел: ').upper().split(' ')
        page = get_page(date)
        courses = parse_page(page)
        for course in courses:
            if course[1] in cur:
                print(format_str(course))
    else:
        print('Выбранная дата еще не наступила')
                   
