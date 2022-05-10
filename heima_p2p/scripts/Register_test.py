import random
import unittest

import requests

from heima_p2p.api import register
from heima_p2p.utils.Utils import assertUtils


class Register(unittest.TestCase):
    def setUp(self):
        self.registerAPI = register.RegisterAPI()
        self.session = requests.session()

    # 当路径参数r为随机小数时，获取图片验证码成功
    def test_getImgCode01(self):
        # 创建随机小数
        num = random.random()
        print(f"num：{num}")
        response = self.registerAPI.getImgCode(self.session, num)
        # print(response.status_code)
        self.assertEqual(200, response.status_code)

    # 当路径参数r为随机整数时，获取图片验证码成功
    def test_getImgCode02(self):
        # 创建随机整数
        num = random.randint(1, 999)
        print(f"num：{num}")
        response = self.registerAPI.getImgCode(self.session, str(num))
        self.assertEqual(200, response.status_code)

    # 当路径参数r为随机字母时，获取图片验证码失败
    def test_getImgCode03(self):
        # 创建随机字母
        d = random.sample("ahhsjksllshjjsjkksk", 5)
        print(f"d：{d}")
        response = self.registerAPI.getImgCode(self.session, d)
        self.assertEqual(400, response.status_code)

    # 当路径参数r为空时，获取图片验证码失败
    def test_getImgCode04(self):
        d = None
        response = self.registerAPI.getImgCode(self.session, d)
        self.assertEqual(400, response.status_code)

    # 所有参数填写正确，获取短信验证码成功
    def test_getSmscode01(self):
        # 创建随机整数
        num = random.randint(1, 999)
        print(f"num：{num}")
        response = self.registerAPI.getImgCode(self.session, str(num))
        self.assertEqual(200, response.status_code)

        response = self.registerAPI.getSmsCode(self.session, "15116248339", "8888")
        self.assertEqual(200, response.status_code)
        self.assertEqual("短信发送成功", response.json()['description'])

    # 图片验证码错误，获取短信验证码失败
    def test_getSmscode02(self):
        # 创建随机整数
        num = random.randint(1, 999)
        print(f"num：{num}")
        response = self.registerAPI.getImgCode(self.session, str(num))
        self.assertEqual(200, response.status_code)

        response = self.registerAPI.getSmsCode(self.session, "15116248339", "6666")
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(100,response.json()['status'])
        assertUtils.assertInfo(self, response, 200, 100, "图片验证码错误")
        # self.assertEqual("图片验证码错误", response.json()['description'])

    # 图片验证码为空，获取短信验证码失败
    def test_getSmscode03(self):
        # 创建随机整数
        num = random.randint(1, 999)
        print(f"num：{num}")
        response = self.registerAPI.getImgCode(self.session, str(num))
        self.assertEqual(200, response.status_code)
        response = self.registerAPI.getSmsCode(self.session, "15116248339", "")
        assertUtils.assertInfo(self, response, 200, 100, "图片验证码错误")

    # 手机号为空，获取短信验证码失败
    def test_getSmscode04(self):
        # 创建随机整数
        num = random.randint(1, 999)
        print(f"num：{num}")
        response = self.registerAPI.getImgCode(self.session, str(num))
        self.assertEqual(200, response.status_code)
        response = self.registerAPI.getSmsCode(self.session, "", "8888")
        self.assertEqual(100, response.json()["status"])

    # 所有参数填写正确有效，注册成功
    def test_register01(self):
        # 创建随机整数
        num = random.randint(1, 999)
        print(f"num：{num}")
        response = self.registerAPI.getImgCode(self.session, str(num))
        self.assertEqual(200, response.status_code)

        response = self.registerAPI.getSmsCode(self.session, "15116248339", "8888")
        assertUtils.assertInfo(self, response, 200, 200, "短信发送成功")

        response = self.registerAPI.register(self.session, "15116248339", "abc123456", "8888",
                                             "666666", "on", "15116248321")
        assertUtils.assertInfo(self, response, 200, 200, "注册成功")

    # 所有必填参数填写正确有效，注册成功
    def test_register02(self):
        # 创建随机整数
        num = random.randint(1, 999)
        print(f"num：{num}")
        response = self.registerAPI.getImgCode(self.session, str(num))
        self.assertEqual(200, response.status_code)
        response = self.registerAPI.getSmsCode(self.session, "15116248323", "8888")
        assertUtils.assertInfo(self, response, 200, 200, "短信发送成功")
        response = self.registerAPI.register(self.session, "15116248323", "abc123456", "8888",
                                             "666666", "on")
        assertUtils.assertInfo(self, response, 200, 200, "注册成功")

    # 图片验证码错误，注册失败
    def test_register03(self):
        # 创建随机整数
        num = random.randint(1, 999)
        print(f"num：{num}")
        response = self.registerAPI.getImgCode(self.session, str(num))
        self.assertEqual(200, response.status_code)
        response = self.registerAPI.getSmsCode(self.session, "15116248323", "8888")
        assertUtils.assertInfo(self, response, 200, 200, "短信发送成功")
        response = self.registerAPI.register(self.session, "15116248323", "abc123456", "6666",
                                             "666666", "on")
        assertUtils.assertInfo(self, response, 200, 100, "验证码错误!")

    # 短信验证码错误，注册失败
    def test_register04(self):
        # 创建随机整数
        num = random.randint(1, 999)
        print(f"num：{num}")
        response = self.registerAPI.getImgCode(self.session, str(num))
        self.assertEqual(200, response.status_code)
        response = self.registerAPI.getSmsCode(self.session, "15116248324", "8888")
        assertUtils.assertInfo(self, response, 200, 200, "短信发送成功")
        response = self.registerAPI.register(self.session, "15116248324", "abc123456", "8888",
                                             "666677", "on")
        assertUtils.assertInfo(self, response, 200, 100, "验证码错误")

    # 手机号已存在，注册失败
    def test_register05(self):
        # 创建随机整数
        num = random.randint(1, 999)
        print(f"num：{num}")
        response = self.registerAPI.getImgCode(self.session, str(num))
        self.assertEqual(200, response.status_code)

        response = self.registerAPI.getSmsCode(self.session, "15116248321", "8888")
        assertUtils.assertInfo(self, response, 200, 200, "短信发送成功")

        response = self.registerAPI.register(self.session, "15116248321", "abc123456", "8888",
                                             "666666", "on")
        assertUtils.assertInfo(self, response, 200, 100, "手机已存在!")

    # 推荐人不存在，注册失败
    def test_register06(self):
        # 创建随机整数
        num = random.randint(1, 999)
        print(f"num：{num}")
        response = self.registerAPI.getImgCode(self.session, str(num))
        self.assertEqual(200, response.status_code)

        response = self.registerAPI.getSmsCode(self.session, "15116248328", "8888")
        assertUtils.assertInfo(self, response, 200, 200, "短信发送成功")

        response = self.registerAPI.register(self.session, "15116248328", "abc123456", "8888",
                                             "666666", "on", "15116248888")
        assertUtils.assertInfo(self, response, 200, 100, "推荐人不存在")

   