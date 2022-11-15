from app import app


def test_api_first():
    response = app.test_client().get('/api/posts/')
    assert response.status_code == 200


def test_api_second():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
