import pytest
from api.v1.views import get_tasks


def test_get_all_questions(client):
    response = client.get('/todo/api/v1.0/tasks')
    assert response.status_code == 200
    assert b'"id":1' in response.data
    assert b'"id":2' in response.data
