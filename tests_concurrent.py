import unittest
from concurrencytest import ConcurrentTestSuite, fork_for_tests


# Load tests from SampleTestCase defined above
runner = unittest.TextTestRunner()
# Run same tests across 4 processes
suite = unittest.TestLoader().discover(start_dir="./tests")
concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(4))
runner.run(concurrent_suite)
