from src.app import create_app


def test_root_endpoint():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    body = response.get_json()
    assert body["status"] == "ok"
    assert body["service"] == "my-app"


def test_health_endpoint():
    app = create_app()
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
