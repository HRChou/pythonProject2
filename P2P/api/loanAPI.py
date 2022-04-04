from P2P import config


class Loan:
    def __init__(self):
        self.loanListUrl = config.BASE_URL + "/loan/loan/listtender"
        self.loanInfoUrl = config.BASE_URL + "/common/loan/loaninfo"
        self.investDataUrl = config.BASE_URL + " /loan/tender/investdata"
        self.investUrl = config.BASE_URL + "/trust/trust/tender"

    # 获取投资产品列表
    def getLoanList(self, session):
        return session.post(self.loanListUrl)

    # 获取投资产品详情
    def getLoanInfo(self, session, id):
        return session.post(self.loanInfoUrl, params={"id": id})

    # 投资数据
    def getInvestData(self, session, id, amount):
        data = {"id": id, "depositCertificate": -1, "amount": amount}
        return session.post(self.investDataUrl, data=data)

    # 开始投资
    def Invest(self, session, id, amount):
        data = {"id": id, "depositCertificate": -1, "amount": amount}
        return session.post(self.investUrl,data = data)
