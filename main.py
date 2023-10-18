from fastapi import FastAPI
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    