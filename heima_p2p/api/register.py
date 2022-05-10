from heima_p2p import config


class RegisterAPI:
    def __init__(self):
        # 获取图片验证码
        self.getImgCodeUrl = config.BASE_URL + "/common/public/verifycode1/{}"
        # 获取短信验证码
        self.getSmsCodeUrl = config.BASE_URL + "/member/public/sendSms"
        # 注册
        self.regUrl = config.BASE_URL + "/member/public/reg"


    # 获取图片验证码
    def getImgCode(self, session, num):
        url = self.getImgCodeUrl.format(num)
        response = session.get(url)
        return response

    # 获取短信验证码
    def getSmsCode(self, session, phone, imgVerifyCode, type="reg"):
        data = {
            "phone": phone,
            "imgVerifyCode": imgVerifyCode,
            "type": type
        }
        return session.post(self.getSmsCodeUrl, data=data)

    # 注册
    def register(self, session, phone, password, verifycode, phone_code,
                 dy_server, invite_phone=None):
        data = {
            "phone": phone,
            "password": password,
            "verifycode": verifycode,
            "phone_code": phone_code,
            "dy_server": dy_server,
            "invite_phone": invite_phone
        }
        return session.post(self.regUrl, data=data)

