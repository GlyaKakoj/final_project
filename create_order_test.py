# Илья Леднев, 8-я когорта - Финальный проект. Инженер по тестированию плюс

# Функция для проверки кода ответа
import send_requests


def test_create_order():
    order_response = send_requests.get_order_information()
    assert order_response.status_code == 200
