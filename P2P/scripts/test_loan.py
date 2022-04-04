import logging
import unittest

import requests

from P2P import utils
from P2P.api.Reg_Login_API import Reg_Login_Main
from P2P.api.authentication import authentication
from P2P.api.loanAPI import Loan
from P2P.utils import assertInfo


class LoanTest(unittest.TestCase):
    session = None

    @classmethod
    def setUpClass(cls):
        cls.session = requests.session()
        cls.loan = Loan()
        cls.p2p_login = Reg_Login_Main()
        cls.authentication = authentication()
        cls.session = requests.Session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    # 获取投资列表
    def test_getLoanList(self):
        response = self.loan.getLoanList(self.session)
        self.assertEqual(200, response.status_code)
        logging.info(response.json())
        self.assertEqual(1, response.json()['page'])

    # 获取投资产品详情
    def test_getLoanInfo(self):
        response = self.loan.getLoanInfo(self.session, 2243)
        logging.info(response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json()["status"])

    # 投资成功
    def test_getInvestData(self):
        response = self.loan.getLoanList(self.session)
        self.assertEqual(200, response.status_code)
        loan_id = response.json()['items'][3]['id']

        response = self.loan.getLoanInfo(self.session, loan_id)
        logging.info(invest_id)
        # logging.info(response.json())
        response = self.p2p_login.login(self.session, "15821030761", "abc123456")
        assertInfo(self, response, 200, 200, '登录成功')

        # 投资
        response = self.loan.Invest(self.session, 2243, 1000)
        data = response.json()['description']['form']
        response = utils.returnDataFromForm(data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("InitiativeTender OK", response.text)
