from heima_p2p import config


class Authorization:
    def __init__(self):
        self.authUrl = config.BASE_URL + "/member/realname/approverealname"
        self.getapproveUrl = config.BASE_URL + "/member/member/getapprove"
        self.trust_regUrl = config.BASE_URL + "/trust/trust/register"

    # 实名认证
    def authorization(self, session, realname, card_id):
        data = {
            "realname": realname,
            "card_id": card_id
        }
        return session.post(self.authUrl, data=data, files={"abc": "abc"})

    # 获取认证信息
    def getApprove(self, session):
        return session.post(self.getapproveUrl)

    # 开户
    def trust_register(self,session):
        return session.post(self.trust_regUrl)

