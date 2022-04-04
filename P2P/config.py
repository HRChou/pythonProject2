import logging
import os
from logging import handlers

# 获取项目根目录绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 项目地址路径
BASE_URL = "http://user-p2p-test.itheima.net"

HEADERS = {
    "Content-Type": "multipart/form-data"
}


def init_log_config():
    # 获取日志对象
    log = logging.getLogger()
    # 设置日志输出级别
    log.setLevel(logging.INFO)
    # 3、创建控制台日志处理器和文件日志处理器
    sh = logging.StreamHandler()

    logfile = BASE_DIR  + "/log" + os.sep + "p2p.log"
    fh = logging.handlers.TimedRotatingFileHandler(logfile, when='M', interval=5, backupCount=5, encoding='UTF-8')
    # 4、设置日志格式，创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 5、将格式化器设置到日志器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 6、将日志处理器添加到日志对象
    log.addHandler(sh)
    log.addHandler(fh)
