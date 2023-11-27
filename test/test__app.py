"""
Test uu_py_test_app.app
"""
from unittest import TestCase

from uu_py_test_app.app import mock_function
from uu_py_test_app.app import _main as main

class Test__App_mock_function(TestCase) :
    
    def test_mock_function(self):
        self.assertIsNone(mock_function())

class Test__App_main(TestCase) :
    def test_main_ok(self):
        self.assertEqual(main(),0)
    
    def test_main_err(self):
        self.assertEqual(main(*["-f"]),1)

class Test__Fail(TestCase) :
    
    def test_failure(self):
        self.fail(msg="forced failure")
