import time
import unittest

from P2P import config
from P2P.lib.HTMLTestRunner import HTMLTestRunner
from P2P.scripts import test_RegLogin_P2P

suite = unittest.TestSuite()
# suite.addTest(test_RegLogin_P2P.P2P_RegLoginTest('test_getVerifyCode'))
suite.addTests(unittest.makeSuite(test_RegLogin_P2P.P2P_RegLoginTest))
fileName = config.BASE_DIR + "/reports/reporter-{}.html".format(time.strftime('%Y-%m-%d %H%M%S'))
# suite = unittest.TestLoader().discover(config.BASE_DIR + '/scripts/', "*test*.py")
with open(fileName,'wb') as f:
    HTMLTestRunner(f).run(suite)