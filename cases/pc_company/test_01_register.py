# -*- coding: utf-8 -*-
"""
    @File: test_01_register.py
    @Desc: 
    @Time: 2021/11/1 下午5:23
    @Author: Wan Wenlong
"""
import pytest
from common.utils import read_csv, csv_to_dict
from common.base_page import BasePage, save_error_screenshot
from common.page_details.login_page import LoginPage


class TestRegister:
    data = read_csv('test_login.csv')

    @save_error_screenshot
    @pytest.mark.register
    @pytest.mark.parametrize('user_info', data[7:])
    def test_resister(self, driver, user_info):
        self.driver = driver
        f = LoginPage(driver)
        data = csv_to_dict(user_info[1])
        driver.get(self.data[1][1])
        f.input_user(data['account'])
        f.input_pwd(data['password'])
        f.click_login()
        assert user_info[2] in driver.page_source, '校验失败'


if __name__ == '__main__':
    pytest.main(['-s', __file__])
