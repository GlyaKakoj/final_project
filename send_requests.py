# Илья Леднев, 8-я когорта - Финальный проект. Инженер по тестированию плюс
import requests
import data
import configuration


# Функция создания нового заказа
def new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)


# Функция получения номера трека заказа
def get_new_order_track():
    return new_order().json()['track']


# Функция получения информации о заказе
# Получаю номер трека(цифры), чтобы использовать конкатенацию строк, перевожу цифры в строку с помощью str
def get_order_information():
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFO + str(get_new_order_track()))
