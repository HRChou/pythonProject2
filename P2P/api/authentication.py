from P2P import config


class authentication:
    def __init__(self):
        self.authenticationUrl = config.BASE_URL + "/member/realname/approverealname"
        self.get_authenticationUrl = config.BASE_URL + "/member/member/getapprove"

    # 实名认证
    def authentication(self, session, realname, card_id):
        data = {
            "realname": realname,
            "card_id": card_id
        }
        return session.post(self.authenticationUrl, data=data, files = {"abc":"abc"})

    # 获取实名认证信息
    def get_authenticationInfo(self,session):
        return session.post(self.get_authenticationUrl)
