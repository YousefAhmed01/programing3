from abc import ABCMeta, abstractmethod

class IBuilder(metaclass=ABCMeta):

    def build_part_a():
        "Build part a"

 
    def build_part_b():
        "Build part b"

   
    def build_part_c():
        "Build part c"

   
    def get_result():
        "Return the final product"

class Builder(IBuilder):

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append('a')
        return self

    def build_part_b(self):
        self.product.parts.append('b')
        return self

    def build_part_c(self):
        self.product.parts.append('c')
        return self

    def get_result(self):
        return self.product

class Product():

    def __init__(self):
        self.parts = []

class Director:

    def construct():
        return Builder()\
            .build_part_a()\
            .build_part_b()\
            .build_part_c()\
            .get_result()

PRODUCT = Director.construct()
print(PRODUCT.parts)
