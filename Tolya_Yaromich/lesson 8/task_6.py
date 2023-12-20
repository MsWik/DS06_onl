import pandas as pd

def cheque(price_list, **purchases):
    purchase_list = [(product, number) for product, number in purchases.items()]

    purchase_list.sort(key=lambda x: x[0])

    cheque_df = pd.DataFrame(purchase_list, columns=['product', 'number'])

    cheque_df['price'] = cheque_df['product'].map(price_list)

    cheque_df['cost'] = cheque_df['price'] * cheque_df['number']
    return cheque_df


products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1,bread=4)
print(result)

