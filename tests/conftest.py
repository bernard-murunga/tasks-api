import pytest
from api.v1.app_init import create_app


@pytest.fixture
def app():
    app = create_app()

    yield app

@pytest.fixture
def client(app):
    return app.test_client()


