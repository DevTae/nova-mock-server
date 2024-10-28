from fastapi import FastAPI
from datetime import datetime

app = FastAPI() # python3 -m uvicorn main:app --reload

@app.get("/v1/nodes")
async def get_nodes():
    timestamp = datetime.utcnow().isoformat()
    
    response_data = {
            "time": timestamp,
            "state": "manageable"
    }

    return response_data

