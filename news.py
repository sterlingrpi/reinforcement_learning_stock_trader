from GoogleNews import GoogleNews

def get_news(search_term, date, field='title', num_searches=5):
    googlenews = GoogleNews(start=date, end=date)
    googlenews.search(search_term)
    results = googlenews.results()

    #print('num results =', len(results))
    # for i in range(len(results)):
    #     print('SEARCH RESULT', i, ':')
    #     for key in results[i]:
    #         print(key, ':', results[i][key])

    strings = []
    for i in range(min(num_searches, len(results))):
        strings.append(results[i][field])
    return strings

if __name__ == '__main__':
    search_term = 'AAPL'
    date = '12/04/2019'
    field = 'title'
    list = get_news(search_term, date, field, num_searches=5)
    for i, string in enumerate(list):
        print(field, i, ':', string)
