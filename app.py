from fastapi import FastAPI, Query
import json
from gnews import GNews
from typing import List




app = FastAPI(title="NEWS APP API ENDPOINT IN FASTAPI")




@app.get("/query/")
async def hello(name: List[str] = Query()):
    news_result = {}
    google_news = GNews()
    for i in name:
        scraped_news = google_news.get_news(i)
        for index in range(len(scraped_news)):
            for key in scraped_news:
                title = key["title"].split('-')[0]
                author = key["title"].split('-')[1]
                news_re = {"heading":key["title"],"url":key["url"],"author":author}
                news_result.update(news_re)
    return {"name":news_result}



# @app.get("/")
# async def read_item(request: Request):
#     dat = json.loads(result_in_json)
#     for i in dat['history']:  
#         link = i['URL']
#         res = link.rsplit('/', 1)[-1]  ##feching the slug part of URLsss!!
#         if res != "" and keyword_filter not in res:   #remove keywords and debrisss!!
#            result_in_list.append(res)    
#     result = result_in_list[-5:]  #get the last 10 results...
#     news_result = []
#     for a in result:
#         google_news = GNews()
#         pakistan_news = google_news.get_news(a)
#         for index in range(len(pakistan_news)):
#             for key in pakistan_news:
#                 title = key["title"].split('-')[0]
#                 author = key["title"].split('-')[1]
#                 news_re = {"heading":key["title"],"url":key["url"],"author":author}
#                 news_result.append(news_re)
#     return {
#         "news_result": news_result
#     }
