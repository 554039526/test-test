# -*- coding: utf-8 -*-
"""
    @File: excel.py
    @Desc: 
    @Time: 2021/11/28 10:48 上午
    @Author: Wan Wenlong
"""
import xlrd  # xlrd==1.2.0, 高版本不支持xlsx格式，安装方法 pip install xlrd==1.2.0
from utils.util import data_path
import os
from utils.common import *


def get_sheet(file):
    file_path = os.path.join(os.path.join(data_path, 'pc_agent'), file)
    try:
        r = xlrd.open_workbook(file_path)
        sheet = r.sheets()[0]
        return sheet
    except Exception as e:
        print(f'文件{file}打开异常！请检查文件是否存在', e)
        return None


def get_data(sheet):
    """
    codeing...
    :param sheet:
    :return:
    """
    res = []
    for x in range(5, sheet.nrows):
        data = sheet.row_values(x)
        if '\r\n' in data:
            list_data = data[1].split(',\r\n')
        else:
            list_data = data[1].split(',\n')

        data_dict = {}
        for n in list_data:
            v = n.split('=')[1]
            if v == 'random_unique_customer_phone':
                v = get_phone(business='customer', unique=True)
            data_dict[n.split('=')[0]] = v
        data_dict['response'] = data[2]
        res.append(data_dict)

    return res


def get_pre_info(sheet):
    url = sheet.row_values(1)[1]  # 获取url

    try:
        # 获取登录账号密码
        login_info = sheet.row_values(2)
        if '\r\n' in login_info:
            list_data = login_info[1].split(',\r\n')
        else:
            list_data = login_info[1].split(',\n')
        login_info_dict = {}
        for n in list_data:
            login_info_dict[n.split('=')[0]] = n.split('=')[1]
    except Exception as e:
        login_info_dict = None

    try:
        # 获取当前用例是否执行
        exe = sheet.row_values(3)[1]
    except Exception as e:
        exe = None

    return url, login_info_dict, exe


if __name__ == '__main__':
    sheet = get_sheet('test_01_login.xlsx')
    print(get_pre_info(sheet))

