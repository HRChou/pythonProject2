import logging
import random
import unittest

import requests

from P2P import utils
from P2P.api.Reg_Login_API import Reg_Login_Main
from P2P.api.authentication import authentication
from P2P.api.trustAPI import TrustAPI
from P2P.utils import assertInfo


class TrustTest(unittest.TestCase):
    session = None

    @classmethod
    def setUpClass(cls):
        cls.p2p = TrustAPI()
        cls.session = requests.session()
        cls.p2p_login = Reg_Login_Main()
        cls.authentication = authentication()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    # 发送开户请求
    def test_trust(self):
        response = self.p2p_login.login(self.session, "15821030761", "abc123456")
        logging.info(response.json())

        response = self.p2p.trust(self.session)
        logging.info(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json()["status"])
        logging.info(response.json()["description"].get('form'))
        # 将第三方接口返回的from表单数据保存到trust_data中
        data = response.json()["description"].get('form')
        response = utils.returnDataFromForm(data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("UserRegister OK", response.text)

    # 充值成功
    def test_recharge(self):
        # 登录已开户成功的账户
        response = self.p2p_login.login(self.session, "15821030761", "abc123456")
        assertInfo(self, response, 200, 200, '登录成功')

        # 获取充值验证码
        r = random.random()
        response = self.p2p.get_recharge_VeriCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

        # 向第三方发送充值请求
        response = self.p2p.recharge(self.session, "5000", "8888")
        logging.info(f"form信息是{response.json()['description']['form']}")
        data = response.json()['description']['form']
        response = utils.returnDataFromForm(data)
        self.assertEqual(200,response.status_code)
        self.assertEqual("NetSave OK", response.text)
