from api.scrape import Vlr
from fastapi import FastAPI
from fastapi.responses import FileResponse



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/news")
def news():
    Vlr.vlr_recent(Vlr)
    return FileResponse("./news.json", media_type="application/json")

