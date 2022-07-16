from get_page import *
from parse_page import *

if __name__ == '__main__':
    page = get_page('16.07.2022')
    print(parse_page(page))

