import importlib

import pytest


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_DIR", str(tmp_path))
    monkeypatch.setenv("APP_GREETING", "Hello")
    import app as app_module

    importlib.reload(app_module)
    return app_module.app.test_client()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_greet_default(client):
    assert client.get("/greet").get_json() == {"message": "Hello, world!"}


def test_greet_name(client):
    assert client.get("/greet?name=Ada").get_json() == {"message": "Hello, Ada!"}


def test_visit_counts_up(client, monkeypatch):
    counter = {"value": 0}

    def fake_incr(key):
        assert key == "visits"
        counter["value"] += 1
        return counter["value"]

    monkeypatch.setattr("app.redis_client.incr", fake_incr)

    response1 = client.get("/visit")
    response2 = client.get("/visit")

    assert response1.status_code == 200
    assert response1.get_json() == {"visits": 1}

    assert response2.status_code == 200
    assert response2.get_json() == {"visits": 2}
def test_info(client):
    response = client.get("/info")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "CENG413 HW-1"
    assert data["greeting"] == "Hello"