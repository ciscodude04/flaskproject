#newsapi
#faa8105f64af4697bddf1d6e0297857e
from newsapi import NewsApiClient
import json

news = NewsApiClient(api_key='faa8105f64af4697bddf1d6e0297857e')

#top_headlines = news.get_top_headlines(q='python', language='en')

#print(json.dumps(top_headlines, indent=4, sort_keys=True))


allheadlines = news.get_everything(q='python', language='en', page_size=2)
print(json.dumps(allheadlines, indent=4, sort_keys=True))