from GoogleNews import GoogleNews
import datetime
import numpy as np

def get_news(date, search_term, field='title', num_searches=5):
    googlenews = GoogleNews(start=date, end=date)
    googlenews.search(search_term)
    results = googlenews.results()
    strings = []
    for i in range(min(num_searches, len(results))):
        strings.append(results[i][field])
    return strings

def get_news_seq(start_date, num_days, search_term, field='title', num_searches=1):
    start_date = start_date.split('/')
    day = int(start_date[0])
    month = int(start_date[1])
    year = int(start_date[2])
    start_date = datetime.date(year=year, month=month, day=day)
    date_list = []
    for x in range(num_days):
        date_list.append((start_date + datetime.timedelta(days=x)).strftime("%m/%d/%Y"))
    news_list = []
    for date in date_list:
        news_list.append(' '.join(get_news(date, search_term, field, num_searches=num_searches)))
    return np.array(news_list)

if __name__ == '__main__':
    news_seq = get_news_seq(start_date='12/04/2019',
                            num_days=10,
                            search_term='AAPL')
    print(news_seq)
