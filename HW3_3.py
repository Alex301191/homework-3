import datetime
from datetime import date, timedelta
import requests
# from pprint import pprint

days_count = timedelta(days=2)

todate = date.today()
fromdate = todate - days_count
to_date = datetime.datetime(todate.year, todate.month, todate.day)
from_date = datetime.datetime(fromdate.year, fromdate.month, fromdate.day)
to_date_unix = int(datetime.datetime.timestamp(to_date))
from_date_unix = int(datetime.datetime.timestamp(from_date))


def get_all_question_about_python():
    count = 0
    url = "https://api.stackexchange.com/2.3/questions"
    page = 1
    # status_code = 0
    # while status_code != 400: # больше 100 вопросов вывести невозможно без токена
    params = {
        'page': page,
        'pagesize': 100,
        'fromdate': from_date_unix,
        'todate': to_date_unix,
        'tagged': 'Python',
        'site': 'stackoverflow'
        }
    response = requests.get(url, params=params)
    question_list = response.json()
    for question in question_list['items']:
        print(question['title'])
        count += 1
        page += 1
    response.raise_for_status()
    # status_code = response.status_code
    # question_list = {}
    print(f'Всего вопросов {count}')


get_all_question_about_python()
