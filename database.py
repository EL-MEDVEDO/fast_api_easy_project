import aiosqlite
from models import Task, TaskUpdate

DB_NAME = "tasks.db"

async def create_table():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            description TEXT,
                            completed BOOLEAN NOT NULL DEFAULT 0)""")
        await db.commit()

async def add_task(task: Task):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)",
                         (task.title, task.description, task.completed))
        await db.commit()


async def update_task_db(task_id: int, task: TaskUpdate):
    async with aiosqlite.connect(DB_NAME) as db:
        sql = "UPDATE tasks SET"
        params = []
        if task.title is not None:
            sql += " title = ?,"
            params.append(task.title)
        if task.description is not None:
            sql += " description = ?,"
            params.append(task.description)
        if task.completed is not None:
            sql += " completed = ?,"
            params.append(task.completed)

        sql = sql.rstrip(",") + " WHERE id = ?"
        params.append(task_id)

        await db.execute(sql, params)
        await db.commit()


async def delete_task(task_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        await db.commit()


async def get_tasks(completed: bool = None) -> list:
    async with aiosqlite.connect(DB_NAME) as db:
        if completed is None:
            cursor = await db.execute("SELECT * FROM tasks")
        else:
            cursor = await db.execute("SELECT * FROM tasks WHERE completed = ?", (completed,))
        rows = await cursor.fetchall()
        return [dict(Task(id=row[0], title=row[1], description=row[2], completed=row[3])) for row in rows]


async def get_task(task_id: int) -> dict:
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT id, title, description, completed FROM tasks WHERE id = ?", (task_id,))
        task = await cursor.fetchone()
        return dict(Task(id=task[0], title=task[1], description=task[2], completed=task[3])) if task else None
