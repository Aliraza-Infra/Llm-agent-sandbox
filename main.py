from fastapi import FastAPI, Request
import yaml
import logging

app = FastAPI()
logging.basicConfig(filename="responses.log", level=logging.INFO)

@app.post("/submit-task")
async def submit_task(request: Request):
    data = await request.body()
    task = yaml.safe_load(data)
    response = {
        "task": task.get("task_name"),
        "response": f"Simulated response to: {task.get('prompt')}"
    }
    logging.info(f"Task: {task.get('task_name')}, Prompt: {task.get('prompt')}, Response: {response['response']}")
    return response
