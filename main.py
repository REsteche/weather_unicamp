import uvicorn
import nest_asyncio

from fastapi import FastAPI
from backend import Scraper

nest_asyncio.apply()  # permission for running asyncio in Jupyter or similar environments

app = FastAPI()


@app.get("/weather/campinas")
async def get_weather_data():
    scrapper = Scraper()
    data = scrapper.scrape_weather_data()
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
