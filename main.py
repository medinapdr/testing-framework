from src.xunit.test_result import TestResult
from tests.my_test import MyTest

if __name__ == "__main__":
    result = TestResult()

    test = MyTest('test_a')
    test.run(result)

    test = MyTest('test_b')
    test.run(result)

    test = MyTest('test_c')
    test.run(result)

    print(result.summary())