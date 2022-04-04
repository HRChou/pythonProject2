import logging
import unittest
import requests

from P2P.api.Reg_Login_API import Reg_Login_Main
from P2P.api.authentication import authentication
from P2P.utils import assertInfo


class Test_authenticationUrl(unittest.TestCase):
    session = None

    @classmethod
    def setUpClass(cls):
        cls.p2p_login = Reg_Login_Main()
        cls.p2p = authentication()
        cls.session = requests.session()

    # 实名认证
    def test_01_authentication(self):
        response = self.p2p_login.login(self.session, "15821030761", "abc123456")
        logging.info(response.json())

        response = self.p2p.authentication(self.session, "周杰伦", "110101199405194236")
        logging.info(response.json())
        assertInfo(self, response, 200, 200, "提交成功!")

    # 姓名为空，认证失败
    def test_02_authentication(self):
        response = self.p2p_login.login(self.session, "15821030762", "abc123456")
        logging.info(response.json())

        response = self.p2p.authentication(self.session, "", "110101199405194236")
        logging.info(response.json())
        assertInfo(self, response, 200, 100, "姓名不能为空!")

    # 身份证号码为空，认证失败
    def test_03_authentication(self):
        response = self.p2p_login.login(self.session, "15821030762", "abc123456")
        logging.info(response.json())
        response = self.p2p.authentication(self.session, "15821030762", "")
        logging.info(response.json())
        assertInfo(self, response, 200, 100, "身份证号不能为空!")

    # 获取认证信息
    def test_034_get_authenticationInfo(self):
        response = self.p2p_login.login(self.session, "15821030761", "abc123456")
        logging.info(response.json())
        response = self.p2p.get_authenticationInfo(self.session)
        logging.info(response.json())
        self.assertEqual(200, response.status_code)
