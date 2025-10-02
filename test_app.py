from app import app

def test_hello_route():
    """Тестує, що головна сторінка повертає статус 200 і правильний контент."""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from Azure" in response.data
