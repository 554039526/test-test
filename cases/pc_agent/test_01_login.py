# -*- coding: utf-8 -*-
"""
    @File: test_01_login.py
    @Desc: 
    @Time: 2021/10/22 上午10:33
    @Author: Wan Wenlong
"""
import pytest
from utils.utils import read_csv, csv_to_dict
from utils.base_page import save_error_screenshot
from utils.page_details.pc_agent.page_01_login import LoginPage


class TestLogin:

    data = read_csv('test_01_login.csv')

    @save_error_screenshot
    @pytest.mark.login
    @pytest.mark.parametrize('user_info', data[7:])
    def test_login(self, driver, user_info):
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





