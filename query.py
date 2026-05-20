
from planet import *
from collect import Collect
def query(collection):
    data = input()
    if (data != "close"):
        try:
            collection.run_query(data)
        except Exception as exception:
            print(exception)
        query(collection)



query(Collect([]))
    