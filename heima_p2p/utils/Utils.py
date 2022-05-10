import json

from bs4 import BeautifulSoup

from heima_p2p import config


class assertUtils:
    def assertInfo(self, response, status_code, status, description):
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(status, response.json()['status'])
        self.assertEqual(description, response.json()['description'])


class ThirdData:
    def returnDataFromThird(self, session, response):
        soup = BeautifulSoup(response.json()['description']['form'], "html.parser")
        url = soup.form['action']
        inputList = soup.find_all('input')
        dic = {}
        for input in inputList:
            dic.setdefault(input['name'], input['value'])
        return session.post(url, data=dic)


# 获取注册数据
def getRegData():
    register_datalist = []
    with open(config.BASE_DIR + "/data/register_data.json", 'rb') as f:
        data = json.load(f)
        for item in data:
            phone = item['phone']
            password = item['password']
            verifycode = item["verifycode"]
            phone_code = item['phone_code']
            dy_server = item["dy_server"]
            invite_phone = item["invite_phone"]
            status_code = item["status_code"]
            status = item["status"]
            description = item['description']
            register_datalist.append(
                (phone, password, verifycode, phone_code, dy_server, invite_phone,status_code, status, description))
    return register_datalist


# 获取登录数据
def getLogindata():
    login_datalist = []
    with open(config.BASE_DIR + "/data/login_data.json", 'rb') as f:
        data = json.load(f)
        for item in data:
            keywords = item['keywords']
            password = item['password']
            status_code = item["status_code"]
            status = item['status']
            description = item['description']
            login_datalist.append((keywords, password, status_code, status, description))
    return login_datalist


