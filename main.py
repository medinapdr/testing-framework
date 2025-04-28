from tests.my_test import MyTest

if __name__ == "__main__":
    test = MyTest('test_a')
    test.run()

    test = MyTest('test_b')
    test.run()

    test = MyTest('test_c')
    test.run()