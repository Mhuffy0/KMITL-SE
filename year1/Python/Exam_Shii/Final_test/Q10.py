# Define abstract classes `Product` and `Electronics`. Then, implement the following concrete classes:
# - **Book**: Costs 100 Baht, with a 10% discount on all purchases.
# - **TV** (inherits from `Electronics`): Costs 8,000 Baht with a 7% VAT.
# - **Laptop** (inherits from `Electronics`): Costs 20,000 Baht with a 7% VAT.
# Write a program to calculate the total cost of the following items:
# - 2 Books
# - 1 TV
# - 1 Laptop
# Hint: Use polymorphism to implement a `calculate_cost()` method in each class

from abc import ABC, abstractclassmethod

class Product(ABC):
    @abstractclassmethod
    def calculate(self):
        pass

class Electronics(Product):
    def __init__(self,price, vat = 0.7):
        self.price = price
        self.vat = vat
        
    def calculate(self):
        return self.price + (self.price * self.vat)
    
class Book(Product):
    def __init__(self,price = 100, discount =0.10):
        self.price = price
        self.dis = discount
        
    def calculate(self):
        return self.price * (1 - self.dis)
    
class TV(Electronics):
    def __init__(self, price = 8000, vat=0.07):
        super().__init__(price, vat)
        
    def calculate(self):
        return super().calculate()
    
class Laptop(Electronics):
    def __init__(self, price = 20000, vat=0.07):
        super().__init__(price, vat)
        
    def calculate(self):
        return super().calculate()
    
items = [Book(), Book(), TV(), Laptop()]
# for item in items:
#     temp = 0
#     temp = item.calculate()
#     print(f"{item} is {temp}")
    
total_cost = sum(item.calculate() for item in items)
print(f"Total cost: {total_cost} Baht")
