class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return ''.join(file.readlines())
        except FileNotFoundError:
            return 'File not found'

    def add(self, *products):
        some_products = self.get_products().splitlines()
        some_names = {line.split(', ')[0] for line in some_products if line}
        for i in products:
            if i.name in products:
                print(f'Product {i.name} is already in the shop')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(i) + '\n')
                print(f'Product {i.name} is append')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())