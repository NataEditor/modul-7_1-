from pprint import pprint

class Product:
    """
    Класс Продукты с атрибутами
    name - название продукта
    weight - общий вес товара
    category - категория товара
    """

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return(f'{self.name}, {self.weight}, {self.category}')


class Shop(Product):
    """
    Класс Продукты с атрибутами

    """

    def __init__(self, name, weight, category, __file_name='products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name

    __file_name = 'products.txt'

    def get_products(self):
        file_Op = open(self.__file_name, 'r')
        s = file_Op.read()
        file_Op.close()
        return s

    def add(self, *product):
        for i in product:
            inf = (str(i))
            file = open(self.__file_name, 'r')
            f = file.read()
            file.close()
            if inf in f:
                print(f'Продукт {inf} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{inf}')
                file.close()


s1 = Shop('',0, '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())