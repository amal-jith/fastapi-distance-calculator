

from fastapi import FastAPI
from math import sqrt

app = FastAPI()

@app.get("/distance")
def calc_distance(lat1: float, lon1: float, lat2: float, lon2: float):

    diff_lat = lat2 - lat1
    diff_lon = lon2 - lon1


    distance = sqrt(diff_lat ** 2 + diff_lon ** 2)


    return {"distance": distance}