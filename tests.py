import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_create_task(): #тест создания таска
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.post("/add_task/", json={"id": 1, "title": "Test Task", "description": "Test Description", "completed": False})
    assert response.status_code == 200
    assert response.json() == {"message": "Task created successfully"}


@pytest.mark.asyncio
async def test_read_task(): #тест чтения задания по индексу
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/tasks/1")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_read_tasks(): #тест чтения всех заданий
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        # Выборка с выполненными заданиями
        response = await ac.get("/tasks/", params={"completed": True})
        assert response.status_code == 200
        tasks = response.json()
        assert all(task["completed"] is True for task in tasks)

        # Выборка с не выполненными заданиями
        response = await ac.get("/tasks/", params={"completed": False})
        assert response.status_code == 200
        tasks = response.json()
        assert all(task["completed"] is False for task in tasks)


@pytest.mark.asyncio
async def test_read_task_not_found(): #тест чтения задания, которого нет
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/tasks/999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_task(): #тест обновления
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.put("/update_task/3", json={"completed": True})
        if response.status_code != 200:
            print(response.content)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_task(): #тест удаления
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.delete("/tasks/1")
        assert response.status_code == 200

    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/tasks/1")
    assert response.status_code == 404
