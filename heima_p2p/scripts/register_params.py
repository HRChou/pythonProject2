import random
import unittest

import requests
from parameterized import parameterized

from demo03 import getSum
from heima_p2p.api import register
from heima_p2p.utils import Utils


def getSumData():
    return [(1, 2, 3), (3, 8, 11), (20, 5, 25)]


class Reg_Test(unittest.TestCase):
    def setUp(self):
        self.verifycode = '8888'
        self.regAPI = register.RegisterAPI()
        self.session = requests.session()

    @parameterized.expand(Utils.getRegData())
    def test_register_params(self, phone, password, verifycode, phone_code, dy_server, invite_phone,
                             status_code, status, description):
        num = random.random()
        self.regAPI.getImgCode(self.session, str(num))
        # self.assertEqual(200, response.status_code)

        self.regAPI.getSmsCode(self.session, phone, self.verifycode)
        # self.assertEqual(status, response.json()["status"])

        response = self.regAPI.register(self.session, phone, password, verifycode, phone_code,
                                        dy_server, invite_phone)
        Utils.assertUtils.assertInfo(self, response, status_code, status, description)


