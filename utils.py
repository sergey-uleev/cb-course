import datetime

def not_in_future(date):
    today = datetime.date.today()
    date = date.split('.')
    date = datetime.date(int(date[2]), int(date[1]), int(date[0]))
    return date.year <= today.year and date.month <= today.month and date.day <= today.day