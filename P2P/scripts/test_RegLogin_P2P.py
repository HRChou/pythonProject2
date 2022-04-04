import logging
import random
import unittest
from time import sleep

import requests

from P2P.api import Reg_Login_API
from P2P.utils import assertInfo


class P2P_RegLoginTest(unittest.TestCase):
    session = None

    @classmethod
    def setUpClass(cls):
        cls.p2p = Reg_Login_API.Reg_Login_Main()
        cls.session = requests.session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    # r为随机小数时执行获取图片验证码用例
    def test01_getVerifyCode(self):
        r = random.random()
        response = self.p2p.get_verifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

    # r为随机整数时执行获取图片验证码用例
    def test02_getVerifyCode(self):
        r = random.randint(1, 100)
        response = self.p2p.get_verifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

    # r为随机字母时执行获取图片验证码用例
    def test03_getVerifyCode(self):
        r = random.sample("abcdefghijklmnopqrstuvwxyz", 5)
        response = self.p2p.get_verifyCode(self.session, str(r))
        self.assertEqual(400, response.status_code)

    # r为空时执行获取图片验证码用例
    def test04_getVerifyCode(self):
        response = self.p2p.get_verifyCode(self.session, "")
        self.assertEqual(404, response.status_code)

    # 执行获取短信验证码成功用例
    def test05_getSmsCode(self):
        # 先获取图片验证码
        r = random.randint(1, 100)
        response = self.p2p.get_verifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

        response = self.p2p.get_SmsCode(self.session, "15821030751", "8888", "reg")
        self.assertEqual(200, response.status_code)
        self.assertEqual("短信发送成功", response.json()['description'])

    # 图片验证码错误，获取短信验证码失败
    def test06_getSmsCode(self):
        # 先获取图片验证码
        r = random.randint(1, 100)
        response = self.p2p.get_verifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)
        response = self.p2p.get_SmsCode(self.session, "15821030751", "6666", "reg")
        self.assertEqual(200, response.status_code)
        self.assertEqual(100, response.json()['status'])

    # 手机号为空，获取短信验证码失败
    def test07_getSmsCode(self):
        # 先获取图片验证码
        r = random.randint(1, 100)
        response = self.p2p.get_verifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

        response = self.p2p.get_SmsCode(self.session, "", "8888", "reg")
        logging.info(response.json())
        self.assertEqual(100, response.json()['status'])

    # 图片验证码为空，获取短信验证码失败
    def test08_getSmsCode(self):
        # 先获取图片验证码
        r = random.randint(1, 100)
        response = self.p2p.get_verifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)
        response = self.p2p.get_SmsCode(self.session, "15821030751", "", "reg")
        assertInfo(self, response, 200, 100, '图片验证码错误')

    # 没有获取图片验证码，获取短信验证码失败
    def test09_getSmsCode(self):
        response = self.p2p.get_SmsCode(self.session, "15821030751", "", "reg")
        assertInfo(self, response, 200, 100, '图片验证码错误')

    # 所有参数填写正确，注册成功
    def test10_register(self):
        # 先获取图片验证码
        r = random.randint(1, 100)
        response = self.p2p.get_verifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)
        # 再获取短信验证码
        response = self.p2p.get_SmsCode(self.session, "15821030761", "8888", "reg")
        assertInfo(self, response, 200, 200, '短信发送成功')

        response = self.p2p.Register(self.session, "15821030761", "abc123456",
                                     "8888", "666666", "on", "15116248321")
        assertInfo(self, response, 200, 200, '注册成功')

    # 所有必填参数填写正确，注册成功
    def test11_register(self):
        # 先获取图片验证码
        r = random.randint(1, 100)
        response = self.p2p.get_verifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)
        # 再获取短信验证码
        response = self.p2p.get_SmsCode(self.session, "15821030762", "8888", "reg")
        assertInfo(self, response, 200, 200, '短信发送成功')
        response = self.p2p.Register(self.session, "15821030762", "abc123456",
                                     "8888", "666666", "on")
        assertInfo(self, response, 200, 200, '注册成功')

    # 图片验证码错误，注册失败
    def test12_register(self):
        # 先获取图片验证码
        r = random.randint(1, 100)
        response = self.p2p.get_verifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)
        # 再获取短信验证码
        response = self.p2p.get_SmsCode(self.session, "15821030763", "8888", "reg")
        assertInfo(self, response, 200, 200, '短信发送成功')
        response = self.p2p.Register(self.session, "15821030763", "abc123456",
                                     "6666", "666666", "on")
        assertInfo(self, response, 200, 100, '验证码错误!')

    # 手机验证码错误，注册失败
    def test13_register(self):
        # 先获取图片验证码
        r = random.randint(1, 100)
        response = self.p2p.get_verifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)
        # 再获取短信验证码
        response = self.p2p.get_SmsCode(self.session, "15821030763", "8888", "reg")
        assertInfo(self, response, 200, 200, '短信发送成功')
        response = self.p2p.Register(self.session, "15821030763", "abc123456",
                                     "8888", "666688", "on")
        assertInfo(self, response, 200, 100, '验证码错误')

    # 密码为空，注册失败
    # def test14_register(self):
    #     # 先获取图片验证码
    #     r = random.randint(1, 100)
    #     response = self.p2p.get_verifyCode(self.session, str(r))
    #     self.assertEqual(200, response.status_code)
    #     # 再获取短信验证码
    #     response = self.p2p.get_SmsCode(self.session, "15821030773", "8888", "reg")
    #     utils.assertInfo(self, response, 200, 200, '短信发送成功')
    #     response = self.p2p.Register(self.session, "15821030773", "",
    #                                  "8888", "666666", "on")
    #     utils.assertInfo(self, response, 200, 100, '密码不能为空')
    # 手机验证码错误，注册失败

    def test14_register(self):
        # 先获取图片验证码
        r = random.randint(1, 100)
        response = self.p2p.get_verifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)
        # 再获取短信验证码
        response = self.p2p.get_SmsCode(self.session, "15821030762", "8888", "reg")
        assertInfo(self, response, 200, 200, '短信发送成功')
        response = self.p2p.Register(self.session, "15821030762", "abc123456",
                                     "8888", "666666", "on")
        logging.info(response.json())
        assertInfo(self, response, 200, 100, '手机已存在!')

    # 登录成功
    def test_15_login(self):
        response = self.p2p.login(self.session, "15821030762", "abc123456")
        assertInfo(self, response, 200, 200, '登录成功')

    # 用户不存在，登录失败
    def test_16_login(self):
        response = self.p2p.login(self.session, "15821030792", "abc123456")
        assertInfo(self, response, 200, 100, '用户不存在')

    # 手机号为空， 登录失败
    def test_17_login(self):
        response = self.p2p.login(self.session, "", "abc123456")
        assertInfo(self, response, 200, 100, '用户名不能为空')

    # 密码为空，登录失败
    def test_18_login(self):
        response = self.p2p.login(self.session, "15116248321", "")
        assertInfo(self, response, 200, 100, '密码不能为空')

    # 密码错误，登录失败
    def test_19_login(self):
        # 输入1次错误密码，提示错误1次
        response = self.p2p.login(self.session, "15116248321", "123456")
        logging.info(response.json())
        assertInfo(self, response, 200, 100, "密码错误1次,达到3次将锁定账户")
        response = self.p2p.login(self.session, "15116248321", "123456")
        logging.info(response.json())
        # 输入2次错误密码，提示错误2次
        assertInfo(self, response, 200, 100, "密码错误2次,达到3次将锁定账户")
        # 输入3次错误密码，提示锁定账户，1分钟后再试
        response = self.p2p.login(self.session, "15116248321", "123456")
        logging.info(response.json())
        assertInfo(self, response, 200, 100, "由于连续输入错误密码达到上限，账号已被锁定，请于1.0分钟后重新登录")
        # 输入正确密码，提示错误锁定
        response = self.p2p.login(self.session, "15116248321", "abc123456")
        assertInfo(self, response, 200, 100, "由于连续输入错误密码达到上限，账号已被锁定，请于1.0分钟后重新登录")
        # 1分钟后输入正确密码，登录成功
        sleep(60)
        response = self.p2p.login(self.session, "15116248321", "abc123456")
        logging.info(response.json())
        assertInfo(self, response, 200, 200, '登录成功')


