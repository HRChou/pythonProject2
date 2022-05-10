from heima_p2p import config


class Login:
    def __init__(self):
        # 登录
        self.loginUrl = config.BASE_URL + "/member/public/login"

    def login(self, session, keywords, password):
        data = {
            "keywords": keywords,
            "password": password
        }
        return session.post(self.loginUrl,data=data)