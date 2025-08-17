from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

# task: 1 and 2

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AnimalResponse(BaseModel):
    id: int
    name: str
    age: int
    adopted: bool
    health_status: str

animal_db = {
    1:{"id": 1, "name": "Рекст", "age": 3, "adopted": False, "health_status": "Healthy"},
    2:{"id": 2, "name": "Барсік", "age": 4, "adopted": True, "health_status": "Healthy"},
}

app = FastAPI(title="Animal Shelter API", version="1.0")

@app.get("/animals/{animals_id}", response_model=AnimalResponse, tags=["Animals"])
def get_animal(animals_id: int):
    if animals_id not in animal_db:
        logger.error(f"Animal with ID {animals_id} not found.")
        raise HTTPException(status_code=404, detail="Animal not found")
    return animal_db[animals_id]


#task: 3

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool

task_db = {
    1: {"id": 1, "title": "Прибрати кімнату", "completed": False},
    2: {"id": 2, "title": "Написати звіт", "completed": True},
}

@app.get("/tasks/{task_id}", response_model=TaskResponse, tags=["Tasks"])
def get_task(task_id: int):
    if task_id > 1000:
        logger.warning(f"Task ID is unusually high: {task_id}")
        raise HTTPException(
            status_code=400, 
            detail="Task ID is too high"
        )

    if task_id not in task_db:
        logger.error(f"Attempt to retrieve a non-existent task: task_id={task_id}")
        raise HTTPException(status_code=404, detail="Task not found.")
    
    logger.info(f"Successful retrieval of task with ID: {task_id}.")
    return task_db[task_id] 