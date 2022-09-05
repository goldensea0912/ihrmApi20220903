# coding=utf-8
import unittest


# from scripts.test_emp_add_params import TestEmpAddParams
from scripts.test_ihrm_login_params import TestIhrmLoginParams

# 运行某个类及类里面的某个方法

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestIhrmLoginParams))
runner = unittest.TextTestRunner()
runner.run(suite)
