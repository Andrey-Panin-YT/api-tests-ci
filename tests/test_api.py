import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "name" in data
    assert "email" in data


def test_create_user():
    payload = {
        "name": "Андрей Сергеевич",
        "username": "andreysergeevich",
        "email": "andrey@example.com"
    }

    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Андрей Сергеевич"
    assert "id" in data


def test_update_user():
    payload = {
        "name": "Андрей Сергеевич Обновлено"
    }

    response = requests.put(f"{BASE_URL}/users/1", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Андрей Сергеевич Обновлено"
    assert data["id"] == 1

