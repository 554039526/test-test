# -*- coding: utf-8 -*-
"""
    @File: page_01_login.py
    @Desc: 
    @Time: 2021/10/29 上午8:36
    @Author: Wan Wenlong
"""
from utils.base_page import BasePage, get_driver
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # 元素定位器
    user = (By.ID, '_easyui_textbox_input1')
    pwd = (By.ID, '_easyui_textbox_input4')
    lg_bt = (By.ID, 'btn-mobile-btn')

    # 元素操作方法
    def input_user(self, value):
        self.input(value, *self.user)

    def input_pwd(self, value):
        self.input(value, *self.pwd)

    def click_login(self):
        self.click(*self.lg_bt)


def login(username, password):
    lg = LoginPage()
    lg.input_user(username)
    lg.input_pwd(password)
    lg.click_login()


if __name__ == '__main__':
    driver = get_driver('chrome')
    driver.get('https://relsagent.joyi.cn/agent/home/ag/login/page')
    login('18703651001', 'Beijing@123')
    # f = LoginPage(driver)
    # f.input_user('18703651001')
    # f.input_pwd('Beijing@123')
    # f.click_login()
