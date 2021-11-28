# -*- coding: utf-8 -*-
"""
    @File: util.py
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
data_path_pc_agent = os.path.join(data_path, 'pc_agent')

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
conf_dir = os.path.join(root_path, 'resources')
conf_path = os.path.join(conf_dir, 'application.ini')

# 截图存放路径
if not os.path.exists(os.path.join(report_path, 'screenshots')):
    os.makedirs(os.path.join(report_path, 'screenshots'))
screenshots_path = os.path.join(report_path, 'screenshots')


def read_csv(filename):
    """
    读取csv文件，每行作为一个list返回到一个大的list中
    :param filename:
    :return:
    """
    file_content_list = []
    file_path = os.path.join(data_path_pc_agent, filename)
    try:
        with open(file_path, 'r') as fp:
            rows = csv.reader(fp)
            for row in rows:
                file_content_list.append(row)
    except Exception as e:
        print(f'未找到文件：{filename}', e)
        return False
    return file_content_list


def csv_to_dict(string: str):
    """
    将数据'account=18703651002,\npassword=Beijing@123'
    转换为dict:   {'account': '18703651019', 'password': 'Beijing@123'}
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


cf = configparser.ConfigParser()
cf.read(conf_path)


def getItemsSection(section_name):
    options_dist = dict(cf.items(section_name))
    return options_dist


# 获取section下某一个option的值
def getOptionValue(section_name, option_name):
    value = cf.get(section_name, option_name)
    return value


if __name__ == '__main__':
    res = csv_to_dict('account=18703651002,\npassword=Beijing@123')
    s = ['使用有效管理员账号登录', 'account=18703651019,\npassword=Beijing@123', '我自有的房源']
    print(csv_to_dict(s[1]))
    res = read_csv('test_02_customer_create.csv')
    print(type(res))
