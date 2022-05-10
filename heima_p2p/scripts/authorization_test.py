import logging
import unittest

import requests
from bs4 import BeautifulSoup

from heima_p2p.api import login
from heima_p2p.api.authorization import Authorization
from heima_p2p.utils.Utils import assertUtils, ThirdData


class TestAuthorization(unittest.TestCase):
    def setUp(self):
        self.authApi = Authorization()
        self.loginAPI = login.Login()
        self.session = requests.session()

    # 姓名和身份证正确有效，认证成功
    def test_auth01(self):
        response = self.loginAPI.login(self.session, "15116248323", "abc123456")
        assertUtils.assertInfo(self, response, 200, 200, "登录成功")

        response = self.authApi.authorization(self.session, "李元昊", "310105199005212872")
        assertUtils.assertInfo(self, response, 200, 200, "提交成功!")

    # 姓名为空，认证失败
    def test_auth02(self):
        response = self.loginAPI.login(self.session, "15116248323", "abc123456")
        assertUtils.assertInfo(self, response, 200, 200, "登录成功")
        response = self.authApi.authorization(self.session, "", "310105199005212872")
        assertUtils.assertInfo(self, response, 200, 200, "姓名不能为空")

    # 获取认证信息
    def test_getapprove(self):
        response = self.loginAPI.login(self.session, "15116248323", "abc123456")
        assertUtils.assertInfo(self, response, 200, 200, "登录成功")

        response = self.authApi.getApprove(self.session)
        self.assertEqual(200, response.status_code)

    # 开户
    def test_trust_register(self):
        response = self.loginAPI.login(self.session, "15116248323", "abc123456")
        assertUtils.assertInfo(self, response, 200, 200, "登录成功")

        response = self.authApi.trust_register(self.session)
        # print(response.json())
        # 初始化bs对象
        # soup= BeautifulSoup(response.json()['description']['form'],"html.parser")
        # url = soup.form['action']
        # inputList = soup.find_all('input')
        # dic = {}
        # for input in inputList:
        #     dic.setdefault(input['name'], input['value'])
        response = ThirdData.returnDataFromThird(self,self.session,response)
        # 发送第三方开户请求
        self.assertEqual(200,response.status_code)




