import json


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.average_price = self.calculate_average_price()

    """магический метод для деления"""

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.price / other

    def calculate_average_price(self):
        return self.price / self.count

    def to_json(self):
        return {
            'name': self.name,
            'price': self.price,
            'count': self.count,
            'average_price': self.average_price
        }

def create_product():
    """Сначала пользователь вводит список продуктов и они добавляются в файл data.json
    цикл бесконечный пока пользователь не введет кнопку 'n'"""
    products = []
    while True:
        name = input('Введите название продукта: ')
        count = int(input('Введите количество штук/грамм: '))
        price = int(input('Введите стоимость в рублях: '))
        product = Product(name, price, count)
        products.append(product)
        page = input('Добавить еще продукты y/n? ').lower()
        if page == 'n':
            break

    products_json = [product.to_json() for product in products]

    with open('data.json', 'a', encoding='utf-8') as file:
        json.dump(products_json, file, indent=2, ensure_ascii=False)
    p = input('хотите составить блюдо y/n? ')
    if p == 'y':
        products = []

        while True:
            product_name = input('Введите название продукта для меню: ')
            quantity = int(input('Введите необходимое количество штук/грамм: '))
            products.append((product_name, quantity))

            more_products = input('Добавить еще продукты y/n? ').lower()
            if more_products == 'n':
                break

        with open('data.json', 'r', encoding='utf-8') as file:
            products_json = json.load(file)
        total_cost = 0
        for product_name, quantity in products:
            for product in products_json:
                if product['name'] == product_name:
                    average_price = product['average_price']
                    total_price = average_price * quantity
                    count = product['count']/quantity
                    print(f'{product_name}: {quantity} шт./гр., средняя цена: {average_price} руб., общая стоимость: {total_price} руб. из имеющихся продуктов вы сможете составить {count}')
                    total_cost += total_price

        print(f'Полная стоимость блюда: {int(total_cost)} руб.')


create_product()

