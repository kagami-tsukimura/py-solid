from singleton import Logger
from test_class import Test

if __name__ == "__main__":
    t1 = Test()
    t2 = Test()
    print(f"Test: {t1 == t2}")
    l1 = Logger()
    l2 = Logger()
    print(f"Singleton: {l1 == l2}")
    l1.output("hello")
    l2.output("world")
