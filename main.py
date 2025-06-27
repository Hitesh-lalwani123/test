from fastapi import FastAPI,BackgroundTasks
app = FastAPI()
from test import scraper

@app.get("/")
def health_check():
    
    return {"msg":"api running"}

@app.get("/scraper_data")
def get_train_data(background_tasks: BackgroundTasks):
    print("scraper running")
    # background_tasks.add_task(scraper)
    res = scraper()
    return res
    # return {"msg":"Scraper running in background"}
    