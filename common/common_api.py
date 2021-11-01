# -*- coding: utf-8 -*-
"""
    @File: common_api.py
    @Desc: 
    @Time: 2021/10/22 上午11:06
    @Author: Wan Wenlong
"""
from common.base_page import *
from common.utils import read_csv


def login(driver, username, password):
    try:
        data = read_csv('test_login.csv')
        url = data[1][1]
        driver.get(url)
        user = find_element(driver=driver, locate_type='XPATH', value='//*[@id="_easyui_textbox_input1"]')
        user.clear()
        user.send_keys(username)
        pwd = find_element(driver=driver, locate_type='XPATH', value='//*[@id="_easyui_textbox_input4"]')
        pwd.clear()
        pwd.send_keys(password)
        submit = find_element(driver=driver, locate_type='XPATH', value='//*[@id="btn-mobile-btn"]')
        submit.click()
        return True
    except Exception:
        return False


if __name__ == '__main__':
    driver = get_driver('chrome')
    login(driver, '18703651001', 'Beijing@123')
