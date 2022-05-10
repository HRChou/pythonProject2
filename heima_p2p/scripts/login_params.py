# 参数化登录
import unittest

import requests
from parameterized import parameterized

from heima_p2p.api import login
from heima_p2p.utils import Utils
from heima_p2p.utils.Utils import assertUtils


class loginPrams(unittest.TestCase):
    def setUp(self):
        self.loginAPI = login.Login()
        self.session = requests.session()
    
    def tearDown(self):
        self.session.close()

    @parameterized.expand(Utils.getLogindata())
    def test_login_params(self, keywords, password, status_code, status, description):
        response = self.loginAPI.login(self.session, keywords, password)
        assertUtils.assertInfo(self, response, status_code, status, description)

