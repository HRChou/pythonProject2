# 断言方法封装
import json

import requests
from bs4 import BeautifulSoup

from P2P import config


def assertInfo(self, response, status_code, status, description):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(status, response.json()['status'])
    self.assertEqual(description, response.json()['description'])


# 第三方返回html格式文件的方法
def returnDataFromForm(data):
    # 解析trust_data数据
    soup = BeautifulSoup(data, "html.parser")
    # form表单的url地址
    return_url = soup.form['action']
    dict = {}
    # 提取input中的数据
    for input in soup.find_all('input'):
        dict.setdefault(input['name'], input['value'])
    # logging.info(dict)
    # 向第三方返回的接口继续发送开户请求
    response = requests.post(return_url, data=dict)
    return response


def getImgVerifyCode():
    with open(config.BASE_DIR + '/data/imgVerifyData.json', "rb") as f:
        # 读取json文件
        data = json.load(f)
        datalist = []
        # 解析json文件，获取test_getImgVerifyCode列表的数据
        dataItem = data['test_getImgVerifyCode']
        for item in dataItem:
            type = item['type']
            status_code = item['status_code']
            # 将数据以元组的格式添加到列表当中
            datalist.append((type, status_code))
        return datalist


def getPhoneCode():
    with open(config.BASE_DIR + "/data/phone_code_data.json", 'rb') as f:
        data = json.load(f)
        datalist = []
        dataItem = data['getPhoneCode']
        for item in dataItem:
            datalist.append((item['phone'],item['imgVerifyCode'],item['type'],item['status_code'], item['status'], item['description']))
        return datalist
