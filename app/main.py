from fastapi import FastAPI, HTTPException
from app.models import FlowRequest
from app.taskManager import FlowManager

app = FastAPI()

@app.post("/flow-manager")
async def run_flow(request: FlowRequest):
    try:
        manager = FlowManager(request.flow)
        results = manager.execute()
        return {
            "status": "completed",
            "flow_id": request.flow.id,
            "execution_history": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
