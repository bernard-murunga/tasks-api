import pytest
from api.v1.views import get_tasks


def test_get_all_questions(client):
    expected_result = {
    "tasks": [
        {
            "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
            "done": False,
            "id": 1,
            "title": "Buy groceries"
        },
        {
            "description": "Need to find a good Python tutorial on the web",
            "done": False,
            "id": 2,
            "title": "Learn Python"
        }
    ]
}
    response = client.get('/todo/api/v1.0/tasks')
    assert response.status_code == 200
    assert b'"id":1' in response.data
    assert b'"id":2' in response.data
    assert expected_result == response.get_json()

def test_post_question(client):
    expected_result = {
    "task": {
        "description": "",
        "done": False,
        "id": 3,
        "title": "Read a book"
        }
    }
    response = client.post('/todo/api/v1.0/tasks', json={"title":"Read a book"})
    assert response.status_code == 201
    assert expected_result == response.get_json()


