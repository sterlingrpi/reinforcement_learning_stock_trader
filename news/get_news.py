from GoogleNews import GoogleNews
import numpy as np

def get_descriptions(search_term, date):
    googlenews = GoogleNews(start=date, end=date)
    googlenews.search(search_term)
    results = googlenews.results()
    descriptions = []
    for i in range(5):
        descriptions.append(results[i]['desc'])
    return descriptions

def search(search_term, date):
    googlenews = GoogleNews(start=date, end=date)
    googlenews.search(search_term)
    results = googlenews.results()
    print('result shape =', np.shape(results))
    i = 0
    for key in results[i]:
        print(key)
        print(results[i][key])

if __name__ == '__main__':
    search_term = 'AAPL'
    date = '12/04/2019'
    descriptions = get_descriptions(search_term=search_term, date=date)

    for description in descriptions:
        print(description)

    search(search_term, date)
