from fastapi import FastAPI
from datetime import datetime

app = FastAPI() # python3 -m uvicorn main:app --reload

count = 0

@app.get("/v1/nodes")
async def get_nodes():
    global count

    timestamp = datetime.utcnow().isoformat()
    
    count += 1
    if count % 5 == 0:
        state = "cleaning"
    else:
        state = "manageable"

    response_data = {
            "time": timestamp,
            "state": state
    }

    return response_data

@app.post("/v1/update")
async def update_metrics():
    response_data = {}
    
    return response_data

