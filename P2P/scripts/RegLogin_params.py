import random
import unittest

import requests
from parameterized import parameterized

from P2P import utils
from P2P.api import Reg_Login_API


class P2P_RegLoginTest(unittest.TestCase):
    session = None

    @classmethod
    def setUpClass(cls):
        cls.p2p = Reg_Login_API.Reg_Login_Main()
        cls.session = requests.session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    # 获取图片验证码
    @parameterized.expand(utils.getImgVerifyCode())
    def test_getImgVerifyCode(self, type, status_code):
        r = ''
        if type == 'float':
            r = str(random.random())
        elif type == 'int':
            r = str(random.randint(1, 9999))
        elif type == 'char':
            r = "".join(random.sample("abcdefghijklmn", 4))
        response = self.p2p.get_verifyCode(self.session, r)
        self.assertEqual(status_code, response.status_code)

    # 获取短信验证码
    @parameterized.expand(utils.getPhoneCode())
    def test_getPhoneCode(self,phone,imgVerifyCode,type,status_code,status,description):
        r = str(random.random())
        response = self.p2p.get_verifyCode(self.session,r)
        self.assertEqual(200,response.status_code)

        response = self.p2p.get_SmsCode(self.session,phone,imgVerifyCode,type)
        utils.assertInfo(self,response,status_code,status,description)
