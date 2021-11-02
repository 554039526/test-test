# -*- coding: utf-8 -*-
"""
    @File: utils.py
    @Desc: 
    @Time: 2021/10/22 上午11:23
    @Author: Wan Wenlong
"""
# imports
import os
import csv
import re
import datetime
import configparser

# 项目根目录
root_path = os.path.dirname(os.path.dirname(__file__))

# 获取测试用例路径
cases_path = os.path.join(root_path, 'cases')

# data存放目录
data_path = os.path.join(root_path, 'data')

# 设置report存放路径
report_path = os.path.join(root_path, 'reports')
now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
report_name = os.path.join(report_path, now + '.html')

# 设置log存放路径
log_path = os.path.join(root_path, 'logs')
log_name = os.path.join(log_path, now + '.log')

# pytest.ini的路径
file_dir = os.path.join(root_path, 'pytest.ini')

# 配置文件的路径
conf_dir = os.path.join(root_path, 'conf')

# 截图存放路径
if not os.path.exists(os.path.join(report_path, 'screenshots')):
    os.makedirs(os.path.join(report_path, 'screenshots'))
screenshots_path = os.path.join(report_path, 'screenshots')


def read_csv(filename):
    file_content_list = []
    file_path = os.path.join(data_path, filename)
    with open(file_path, 'r') as fp:
        rows = csv.reader(fp)
        for row in rows:
            file_content_list.append(row)
    return file_content_list


def csv_to_dict(string: str):
    """
    将数据'account=18703651002,\npassword=Beijing@123'转换为dict
    :param string:
    :return:
    """
    result = {}
    s = re.split(',\n', string)
    for data in s:
        d = data.split('=')
        result.update({d[0]: d[1]})
    return result


def get_data(group_name, key, file=file_dir):
    """
    :param group_name:
    :param key:
    :param file: file不传默认读pytest.ini
    :return:
    """
    if not os.path.exists(file):
        file = os.path.join(conf_dir, file)
    conf = configparser.ConfigParser()
    conf.read(file, 'utf8')
    r = conf.get(group_name, key)
    res = r.split('\n')
    if len(res) == 1:
        return res[0]
    return res

# if __name__ == '__main__':
#     res = csv_to_dict('account=18703651002,\npassword=Beijing@123')
#
#     res = get_data('test_login.csv')
#     print(res)
