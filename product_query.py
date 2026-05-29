
from product import *
from product_collect import Shop
def query(collection):
    data = input()
    if (data != "close"):
        try:
            collection.run_query(data)
        except Exception as exception:
            print(exception)
        query(collection)


def products():
    query(Shop([]))
    