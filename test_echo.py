import pytest
import requests

# Базовый URL тестируемого сервиса Postman Echo
BASE_URL = "https://postman-echo.com"


def test_get_status_code():
    """Тест 1: Проверка успешного статус-кода для GET-запроса."""
    response = requests.get(f"{BASE_URL}/get")
    assert response.status_code == 200


def test_get_with_query_params():
    """Тест 2: GET-запрос с query-параметрами.

    Проверяем, что сервер возвращает переданные параметры обратно в ключе 'args'.
    """
    payload = {"course": "qa", "level": "automation"}
    response = requests.get(f"{BASE_URL}/get", params=payload)

    assert response.status_code == 200
    json_data = response.json()
    assert json_data["args"]["course"] == "qa"
    assert json_data["args"]["level"] == "automation"


def test_post_raw_text():
    """Тест 3: POST-запрос с отправкой обычной строки (Text/Plain)."""
    text_data = "Hello from PyCharm CI CD"
    response = requests.post(f"{BASE_URL}/post", data=text_data)

    assert response.status_code == 200
    assert response.json()["data"] == text_data


def test_post_json_payload():
    """Тест 4: POST-запрос с отправкой JSON-структуры."""
    json_data = {"status": "success", "code": 100}
    response = requests.post(f"{BASE_URL}/post", json=json_data)

    assert response.status_code == 200
    # Проверяем, что отправленный JSON корректно распознан сервером в ключе 'json'
    assert response.json()["json"]["status"] == "success"
    assert response.json()["json"]["code"] == 100


def test_post_with_headers():
    """Тест 5: POST-запрос с кастомным заголовком (Header)."""
    custom_headers = {"X-Test-Suite": "PytestEcho"}
    response = requests.post(f"{BASE_URL}/post", headers=custom_headers)

    assert response.status_code == 200
    # Сервер возвращает заголовки в нижнем регистре
    assert response.json()["headers"]["x-test-suite"] == "PytestEcho"
