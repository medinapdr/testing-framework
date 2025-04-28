from src.xunit.test_result import TestResult
from tests.test_case_test import TestCaseTest

if __name__ == "__main__":
    result = TestResult()

    test = TestCaseTest('test_result_success_run')
    test.run(result)

    test = TestCaseTest('test_result_failure_run')
    test.run(result)

    test = TestCaseTest('test_result_error_run')
    test.run(result)

    test = TestCaseTest('test_result_multiple_run')
    test.run(result)

    test = TestCaseTest('test_was_set_up')
    test.run(result)

    test = TestCaseTest('test_was_run')
    test.run(result)

    test = TestCaseTest('test_was_tear_down')
    test.run(result)

    test = TestCaseTest('test_template_method')
    test.run(result)

    print(result.summary())