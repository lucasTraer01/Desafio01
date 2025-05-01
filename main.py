from fastapi import FastAPI, HTTPException
from .models import ScrapeRequest
from .tasks import send_scrape_task, get_task_status

app = FastAPI()

@app.post("/scrape")
async def scrape(request: ScrapeRequest):
    task_id = await send_scrape_task(request.cnpj)
    return {"task_id": task_id}

@app.get("/results/{task_id}")
async def get_results(task_id: str):
    status = await get_task_status(task_id)
    if not status:
        raise HTTPException(status_code=404, detail="Task not found")
    return status