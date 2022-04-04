from P2P import config


class TrustAPI:
    def __init__(self):
        self.trustUrl = config.BASE_URL + "/trust/trust/register"
        self.rechargeVerifyCode_Url = config.BASE_URL + "/common/public/verifycode/{}"
        self.rechargeUrl = config.BASE_URL + "/trust/trust/recharge"

    # 发送开户
    def trust(self, session):
        return session.post(self.trustUrl)

    # 获取充值验证码
    def get_recharge_VeriCode(self, session, r):
        return session.get(self.rechargeVerifyCode_Url.format(r))

    # 充值
    def recharge(self, session, amount, valicode):
        data = {
            "paymentType": "chinapnrTrust",
            "formStr": "reForm",
            "amount": amount,
            "valicode": valicode
        }
        return session.post(self.rechargeUrl, data=data)
