from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from browser_history import get_history
import json
import datetime
from gnews import GNews


outputs = get_history()


i = 0
result_in_list = []
checking_for_none = ""
result_in_json = str(outputs.to_json())
keyword_filter = "+"



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")



@app.get("/")
async def read_item(request: Request):
    dat = json.loads(result_in_json)
    for i in dat['history']:  
        link = i['URL']
        res = link.rsplit('/', 1)[-1]  ##feching the slug part of URLsss!!
        if res != "" and keyword_filter not in res:   #remove keywords and debrisss!!
           result_in_list.append(res)    
    result = result_in_list[-5:]  #get the last 10 results...
    news_result = []
    for a in result:
        google_news = GNews()
        pakistan_news = google_news.get_news(a)
        for index in range(len(pakistan_news)):
            for key in pakistan_news:
                title = key["title"].split('-')[0]
                author = key["title"].split('-')[1]
                news_re = {"heading":key["title"],"url":key["url"],"author":author}
                news_result.append(news_re)
    return templates.TemplateResponse("index.html", {"request":request,"news_result":news_result})
