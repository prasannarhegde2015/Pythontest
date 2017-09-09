import unittest
from pyunit import ServiceNow

 
# get all tests from SearchText and HomePageTest class
tcrun1 = unittest.TestLoader().loadTestsFromTestCase(ServiceNow)

 
# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([tcrun1])
 
# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)