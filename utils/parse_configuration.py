# -*- coding: utf-8 -*-
"""
    @File: parse_configuration.py
    @Desc: 
    @Time: 2021/11/25 下午3:57
    @Author: Wan Wenlong
"""
from utils.util import conf_path
from configparser import ConfigParser


cf = ConfigParser()
cf.read(conf_path)


# 获取某section的所有信息，以字典形式返回，[login]
def getItemsSection(section_name):
    options_dist = dict(cf.items(section_name))
    return options_dist


# 获取section下某一个option的值
def getOptionValue(section_name, option_name):
    value = cf.get(section_name, option_name)
    return value


if __name__ == "__main__":

    print(getItemsSection("sqlserver"))
    print(getOptionValue("sqlserver", "password"))
