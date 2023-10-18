from fastapi import FastAPI
from model.update_data import UpdateData
import json

app = FastAPI()

@app.get("/")
async def root():
    return "ok"


@app.get("/data")
async def data():
    data = {}
    with open("./static/data.json", "r") as json_file:
        data = json.load(json_file)
    return data

@app.put("/data")
async def update_data(rq: UpdateData):
    data = {}
    with open("./static/data.json", "r") as file:
        data = json.load(file)
    data['data']["auth"] = rq.auth
    data['data']['state_management'] = rq.state_management
    data['data']['market_place'] = rq.market_place
    data['data']['questionnaire'] = rq.questionnaire
    data['data']['persional'] = rq.persional
    data['data']['bookings'] = rq.bookings
    data['data']['casesapp'] = rq.casesapp
        
    with open("./static/data.json", 'w') as file:
        json.dump(data, file, indent=4)
    
    return data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    