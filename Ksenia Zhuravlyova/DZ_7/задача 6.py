#products = ['bread', 'milk', 'soda', 'cream']
#prices = [37, 58, 99, 72]
#price_list = pd.Series(prices, products)
#result = cheque(price_list, soda=3, milk=2, cream=1)
#print(result)
# Вывод
#   product  price  number  cost
# 0   cream     72       1    72
# 1    milk     58       2   116
# 2    soda     99       3   297

import pandas as pd

def cheque(price_list, **items):
    df = pd.DataFrame({'product': list(items.keys()), 'number': list(items.values())})
    df['price'] = df['product'].apply(lambda x: price_list.get(x))
    df['cost'] = df['price'] * df['number']
    df.sort_values(by='product', inplace=True)
    return df

products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)

result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)

