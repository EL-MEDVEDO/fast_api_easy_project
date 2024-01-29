from fastapi import FastAPI, HTTPException
from models import Task, TaskUpdate
from database import create_table, add_task, get_tasks,  get_task, update_task_db, delete_task

app = FastAPI()

@app.on_event("startup")
async def startup():
    await create_table()


@app.post("/add_task/")
async def create_task(task: Task):
    await add_task(task)
    return {"message": f"Task created successfully"}


@app.put("/update_task/{task_id}")
async def update_task(task_id: int, task: TaskUpdate):
    await update_task_db(task_id, task)
    return {"message": f"Task {task_id} updated successfully"}


@app.get("/tasks/")
async def read_tasks(completed: bool = None):
    tasks = await get_tasks(completed)
    return tasks


@app.get("/tasks/{task_id}")
async def read_task(task_id: int):
    task = await get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return task


@app.delete("/tasks/{task_id}")
async def delete_task_endpoint(task_id: int):
    await delete_task(task_id)
    return {"message": f"Task {task_id} deleted successfully"}
