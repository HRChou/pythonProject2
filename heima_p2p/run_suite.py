import time
import unittest

from heima_p2p import config
from heima_p2p.lib.HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover(config.BASE_DIR+"/scripts/", pattern="*.py")
fileName = config.BASE_DIR+"/reports/report{}.html".format(time.strftime("%Y-%m-%d-%H%M%S"))
with open(fileName, "wb") as f:
    HTMLTestRunner(f,title='黑马p2p测试报告').run(suite)
