import unittest

import requests
from parameterized import parameterized

from heima_p2p.api.login import Login
from heima_p2p.utils import Utils
from heima_p2p.utils.Utils import assertUtils


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.loginAPI = Login()
        self.session = requests.session()

    # 所有参数填写正确，登录成功
    def test_login01(self):
        response = self.loginAPI.login(self.session, "15116248323", "abc123456")
        assertUtils.assertInfo(self, response, 200, 200, "登录成功")

    # 手机号不存在，登录失败
    def test_login02(self):
        response = self.loginAPI.login(self.session, "15116248866", "abc123456")
        assertUtils.assertInfo(self, response, 200, 100, '用户不存在')

    # 密码为空，登录失败
    def test_login03(self):
        response = self.loginAPI.login(self.session, "15116248321", "")
        assertUtils.assertInfo(self, response, 200, 100, '密码不能为空')

    # 连续输入错误密码，登录失败,被锁定60秒后重新输入正确密码登录成功
    # def test_login04(self):
    #     # 输入一次错误密码，登录失败
    #     response = self.loginAPI.login(self.session, "15116248321", "abc123")
    #     assertUtils.assertInfo(self, response, 200, 100, '密码错误1次,达到3次将锁定账户')
    #     # 输入二次错误密码，登录失败
    #     response = self.loginAPI.login(self.session, "15116248321", "abc123")
    #     assertUtils.assertInfo(self, response, 200, 100, '密码错误2次,达到3次将锁定账户')
    #     # 输入一次错误密码，登录失败
    #     response = self.loginAPI.login(self.session, "15116248321", "abc123")
    #     assertUtils.assertInfo(self, response, 200, 100, '由于连续输入错误密码达到上限，账号已被锁定，请于1.0分钟后重新登录')
    #     # 输入正确密码，登录失败，需等待60秒才能重新登录
    #     response = self.loginAPI.login(self.session, "15116248321", "abc123456")
    #     assertUtils.assertInfo(self, response, 200, 100, '由于连续输入错误密码达到上限，账号已被锁定，请于1.0分钟后重新登录')
    #     sleep(60)
    #     response = self.loginAPI.login(self.session, "15116248321", "abc123456")
    #     assertUtils.assertInfo(self, response, 200, 200, '登录成功')


