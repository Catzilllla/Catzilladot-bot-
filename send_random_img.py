import requests
from telegram import Bot


bot = Bot(token='5306488432:AAHSUp-jzHTOGqbv9NOlsJfLfelCY8dbrdE')
URL = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(URL).json()
# Рассмотрим структуру и содержимое переменной response
print(response)

# Посмотрим, какого типа переменная response
print(type(response))

# response - это список. А какой длины?
print(len(response))

# Посмотрим, какого типа первый элемент
print(type(response[0]))
