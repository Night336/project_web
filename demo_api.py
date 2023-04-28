import requests
import json

url = "http://localhost:8080/api/v1/login"  # адрес, на который отправляется запрос
headers = {"Content-Type": "application/json"}  # заголовок с указанием формата данных
data = {"email": "bbb@bbb.bb", "password": "bbb"}  # JSON-данные для отправки

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    rep = response.json()
    token = rep["token"]
    params = {"token": token}

    url = "http://localhost:8080/api/v1/products"
    response = requests.post(url, headers=headers, params=params)
    print(response.json())

    url = "http://localhost:8080/api/v1/cart"
    response = requests.get(url, headers=headers, params=params)
    print(response.json())

    # url = "http://localhost:8080/api/v1/cart/add"
    # data = {"product_id": 1,
    #         "quantity": 5}
    # response = requests.post(url, headers=headers, params=params, json=data)
    # print(response.json())

    # url = "http://localhost:8080/api/v1/cart/del"
    # data = {"order_id": 10}
    # response = requests.post(url, headers=headers, params=params, json=data)
    # print(response.json())

    # url = "http://localhost:8080/api/v1/cart"
    # response = requests.get(url, headers=headers, params=params)
    # print(response.json())
