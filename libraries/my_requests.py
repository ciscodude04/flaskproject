#newsapi
#faa8105f64af4697bddf1d6e0297857e
from newsapi import NewsApiClient
import json, os

password = os.environ.get('newsAPI_password')

newsapi = NewsApiClient(password)


#print(json.dumps(top_headlines, indent=4, sort_keys=True))

def gettopheadlines():
    #top_headlines = news.get_top_headlines(q='python', language='en')
    pass

def getSources():
    sources = newsapi.get_sources(country='us', language='en')
    length = len(sources["sources"])
    for i in range(0, length):
        id = sources["sources"][i]["id"]
        print(f'{id}')

def all_headlines():
    allheadlines = newsapi.get_everything(q='cor', language='en' , page=1 )
    length = allheadlines["totalResults"]
    for i in range(0, 19):
        description = allheadlines["articles"][i]["description"]
        publication = allheadlines["articles"][i]["publishedAt"]
        title = allheadlines["articles"][i]["title"]        
        print(f'''
        Title: {title}
        Publication Date: {publication}
        Description: {description}
        ''')

