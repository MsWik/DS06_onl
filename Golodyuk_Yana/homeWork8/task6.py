# 6
# В местном магазине решили добавить анализ данных и каждый чек представлять в виде DataFrame.
# Прайс-лист уже сформирован в виде объекта Series, где индексами являются названия,
# а значениями — цены.
# Напишите функцию, cheque, которая принимает прайс-лист и список покупок
# в виде неопределённого количества именованных параметров
# (ключ — название товара, значение — количество).
# Функция должна вернуть объект DataFrame со столбцами:
# наименование продукта (product);
# цена за единицу (price);
# количество (number);
# итоговая цена (cost). Строки чека должны быть отсортированы по названию продуктов
# в лексикографическом порядке.

import pandas as pd


def cheque(price_list, **kwargs):
    df = pd.DataFrame()
    df["product"] = kwargs.keys()
    df["price"] = df["product"].apply(lambda x: price_list[x])
    df["number"] = df["product"].apply(lambda x: kwargs[x])
    df["cost"] = df.apply(lambda x: x["price"] * x["number"], axis=1)
    return df.sort_values(by=["product"])


products = ["bread", "milk", "soda", "cream"]
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)
