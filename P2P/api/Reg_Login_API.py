import bs4 as beautifulsoup4

from P2P import config


class Reg_Login_Main:
    # 初始化接口地址
    def __init__(self):
        self.get_ImgVerifyCodeUrl = config.BASE_URL + "/common/public/verifycode1/{}"
        self.get_SMSCodeUrl = config.BASE_URL + "/member/public/sendSms"
        self.regUrl = config.BASE_URL + "/member/public/reg"
        self.loginUrl = config.BASE_URL + "/member/public/login"


    # 获取图片验证码
    def get_verifyCode(self, session, r):
        response = session.get(self.get_ImgVerifyCodeUrl.format(r))
        return response

    # 获取短信验证码
    def get_SmsCode(self, session, phone, imgVerifyCode, type):
        data = {"phone": phone, "imgVerifyCode": imgVerifyCode, "type": type}
        return session.post(self.get_SMSCodeUrl, data=data)

    # 注册
    def Register(self, session, phone, password, verifycode, phone_code, dy_server, invite_phone=""):
        data = {
            "phone": phone,
            "password": password,
            "verifycode": verifycode,
            "phone_code": phone_code,
            "dy_server": dy_server,
            "invite_phone": invite_phone
        }

        return session.post(self.regUrl, data=data)

    # 登录
    def login(self, session, keywords, password):
        return session.post(self.loginUrl, params={"keywords": keywords, "password": password})



