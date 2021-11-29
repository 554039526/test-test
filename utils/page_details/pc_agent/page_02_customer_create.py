# -*- coding: utf-8 -*-
"""
    @File: page_02_customer_create.py
    @Desc: 
    @Time: 2021/11/16 10:22 下午
    @Author: Wan Wenlong
"""
from utils.base_page import BasePage, get_driver
from selenium.webdriver.common.by import By
import time


class CustomerCreate(BasePage):
    # 元素定位器
    customer_module = (By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div')  # 顶部菜单"客户"
    create_customer = (By.XPATH, '//*[@id="side-menu"]/div[27]')  # 左侧菜单"新增客户"
    create_customer_frame = (By.XPATH, '//*[@id="tabs"]/div[2]/div[3]/div/iframe')
    customer_source = (By.XPATH, '//*[@id="_easyui_textbox_input2"]')
    customer_name = (By.ID, '_easyui_textbox_input3')
    customer_sex_male = (By.ID, '_easyui_radiobutton_2')
    customer_sex_female = (By.ID, '_easyui_radiobutton_3')
    customer_born_date = (By.ID, '_easyui_textbox_input14')
    customer_occupation = (By.ID, '_easyui_textbox_input4')
    customer_phone_master = (By.ID, '_easyui_textbox_input5')
    customer_phone_backup = (By.ID, '_easyui_textbox_input6')
    other_contact = (By.ID, '_easyui_textbox_input7')
    vx = (By.ID, '_easyui_textbox_input8')
    email = (By.ID, '_easyui_textbox_input9')
    address = (By.ID, '_easyui_textbox_input10')
    customer_house_demander = (By.XPATH, '//*[@id="cust-customer-type"]/div/div/span[1]/label')
    customer_house_provide = (By.XPATH, '//*[@id="cust-customer-type"]/div/div/span[2]/label')
    note = (By.ID, '_easyui_textbox_input11')
    submit = (By.ID, 'btn-submit')
    close = (By.CSS_SELECTOR,
             '#tabs > div.tabs-header.tabs-header-narrow > div.tabs-wrap > ul > li.tabs-selected > a.tabs-close')

    # 元素操作方法
    def switch_create_customer(self):
        self.click(*self.customer_module)
        self.click(*self.create_customer)
        self.switch_to_frame(*self.create_customer_frame)

    def input_customer_source(self, value):
        self.input(value, *self.customer_source)

    def input_customer_name(self, value):
        self.input(value, *self.customer_name)

    def input_customer_phone_master(self, value):
        self.input(value, *self.customer_phone_master)

    def select_customer_house_property(self, value):
        if value == 'demander':
            self.execute_js('arguments[0].scrollIntoView();', *self.customer_house_demander)
            self.click(*self.customer_house_demander)
        if value == 'provider':
            self.execute_js('arguments[0].scrollIntoView();', *self.customer_house_provide)
            self.click(*self.customer_house_provide)

    def click_submit(self):
        self.click(*self.submit)

    def close_current_tab(self):
        self.switch_to_parent_frame()
        self.click(*self.close)

# class LoginPage(BasePage):
#     # 元素定位器
#     user = (By.ID, '_easyui_textbox_input1')
#     pwd = (By.ID, '_easyui_textbox_input4')
#     lg_bt = (By.ID, 'btn-mobile-btn')
#
#     # 元素操作方法
#     def input_user(self, value):
#         self.input(value, *self.user)
#
#     def input_pwd(self, value):
#         self.input(value, *self.pwd)
#
#     def click_login(self):
#         self.click(*self.lg_bt)


# if __name__ == '__main__':
#     driver = get_driver('chrome')
#     driver.get('https://relsagent.joyi.cn/agent/home/ag/login/page')
#     f = LoginPage(driver)
#     f.input_user('18703651001')
#     f.input_pwd('Beijing@123')
#     f.click_login()
#     f1 = CustomerCreate(driver)
#     f1.switch_create_customer()
#     f1.input_customer_source('source')
#     f1.input_customer_name('张三')
#     f1.input_customer_phone_master('13300001236')
#     f1.select_customer_house_need()
#     f1.click_submit()
#     time.sleep(5)
#     assert '客户创建成功！' in driver.page_source
#     driver.quit()





