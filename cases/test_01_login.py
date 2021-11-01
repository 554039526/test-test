# -*- coding: utf-8 -*-
"""
    @File: test_01_login.py
    @Desc: 
    @Time: 2021/10/22 上午10:33
    @Author: Wan Wenlong
"""
import pytest
from common.utils import read_csv, csv_to_dict
from common.base_page import get_driver
from common.page_details.login_page import LoginPage


class TestLogin:

    data = read_csv('test_login.csv')
    driver = get_driver('chrome')
    f = LoginPage(driver)

    def setup_class(self):
        pass

    def teardown_class(self):
        self.driver.quit()

    @f.error_screen()
    @pytest.mark.login
    @pytest.mark.parametrize('user_info', data[7:])
    def test_login(self, user_info):
        data = csv_to_dict(user_info[1])
        self.driver.get(self.data[1][1])
        self.f.input_user(data['account'])
        self.f.input_pwd(data['password'])
        self.f.click_login()
        assert user_info[2] in self.driver.page_source, '校验失败'


if __name__ == '__main__':
    pytest.main(['-s', __file__])





