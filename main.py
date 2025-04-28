from src.xunit.test_loader import TestLoader
from src.xunit.test_result import TestResult
from src.xunit.test_runner import TestRunner
from src.xunit.test_suite import TestSuite
from tests.test_case_test import TestCaseTest
from tests.test_loader_test import TestLoaderTest
from tests.test_suite_test import TestSuiteTest

if __name__ == "__main__":
    loader = TestLoader()
    suite = loader.make_suite(TestLoaderTest)

    runner = TestRunner()
    runner.run(suite)