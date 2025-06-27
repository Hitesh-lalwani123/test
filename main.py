from fastapi import FastAPI,BackgroundTasks
app = FastAPI()
from test import scraper

@app.get("/")
def health_check():
    print("scraper running")
    res = scraper()
    
    return {"msg":res}
    