import pandas as pd


def cheque(price_list: pd.Series, **kwargs) -> pd.DataFrame:
    data = {
        'product': kwargs.keys(),
        'price': price_list[kwargs.keys()].values,
        'number': kwargs.values(),
        'cost': [price*number for price, number in zip(price_list[kwargs.keys()].values, kwargs.values())]
    }
    result = pd.DataFrame(data, columns=['product', 'price', 'number', 'cost'])
    result.sort_values('product', inplace=True)
    result.reset_index(drop=True, inplace=True)
    return result


def main():
    products = ['bread', 'milk', 'soda', 'cream']
    prices = [37, 58, 99, 72]
    price_list = pd.Series(prices, products)
    result = cheque(price_list, soda=3, milk=2, cream=1)
    print(result)


if __name__ == '__main__':
    main()
