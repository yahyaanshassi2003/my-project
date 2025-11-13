import pytest
from app import create_app
from database.db import init_db, get_db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['DATABASE'] = 'test.db'
    with app.app_context():
        init_db()
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_add_idea(client):
    rv = client.post('/add', data={'title': 'Test Idea', 'description': 'Just testing'}, follow_redirects=True)
    assert b'Idea added successfully!' in rv.data
