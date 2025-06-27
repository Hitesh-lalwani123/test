from fastapi import FastAPI,BackgroundTasks
app = FastAPI()
from test import scraper

@app.get("/")
def health_check():
    
    return {"msg":"api running"}

@app.get("/scraper_data")
def health_check():
    print("scraper running")
    res = scraper()
    print(res)
    return res
    