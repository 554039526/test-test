# -*- coding: utf-8 -*-
"""
    @File: base_page.py
    @Desc: 
    @Time: 2021/10/22 上午9:51
    @Author: Wan Wenlong
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from utils.utils import *
import time
import functools


def get_driver(browser='chrome'):
    driver = None
    if browser in ['chrome', 'Chrome', 'CHROME']:
        driver = webdriver.Chrome()

    elif browser in ['firefox', 'FIREFOX', 'Firefox']:
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver


def save_error_screenshot(func):
    """ 装饰方法异常时进行保存截图 """
    @functools.wraps(func)
    def wrapper(obj, *args, **kwargs):
        try:
            res = func(obj, *args, **kwargs)
            return res
        except Exception as err:
            if not os.path.exists(os.path.join(screenshots_path, str(now))):
                os.makedirs(os.path.join(screenshots_path, str(now)))
            obj.driver.save_screenshot(os.path.join(os.path.join(screenshots_path, str(now)), f'{time.time()}.png'))
            raise err
    return wrapper


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def find_element(self, locate_type, value, error_msg=None, timeout=30):
        """
        调用：
            driver = webdriver.Chrome()
            driver.get('xxx')
            find_element(locate_type='XPATH', value='//*[@id="pwdFrm"]', timeout=30, error_msg='cannot find')
        返回：
            <class 'selenium.webdriver.remote.webelement.WebElement'>
        :param locate_type:
        :param value:
        :param timeout:
        :param error_msg:
        :return:
        """
        locate_type = locate_type.lower()
        if not error_msg:  # 设置默认的 error_msg
            error_msg = f'元素未找到: {value}'
        try:
            element = WebDriverWait(driver=self.driver, timeout=timeout). \
                until(method=lambda e: self.driver.find_element(by=locate_type, value=value), message=error_msg)
            return element
        except Exception as msg:
            return msg

    def find_elements(self, locate_type, value, error_msg=None, timeout=30):
        """
        调用：
        driver = webdriver.Chrome()
        driver.get('xxx')
        find_elements(locate_type='XPATH', value='//*[@id="pwdFrm"]', timeout=30, error_msg='cannot find')
        返回：
            <class 'list'>
        :param locate_type:
        :param value:
        :param timeout:
        :param error_msg:
        :return:
        """
        locate_type = locate_type.lower()
        if not error_msg:  # 设置默认的 error_msg
            error_msg = f'元素未找到: {value}'

        try:
            element = WebDriverWait(driver=self.driver, timeout=timeout).\
                until(method=lambda e: self.driver.find_elements(by=locate_type, value=value), message=error_msg)
            return element
        except Exception as msg:
            return msg

    def input(self, value, *args):
        """
        指定输入框输入内容
        :param value:
        :param args: *(By.ID, 'user')
        :return:
        """
        element = self.driver.find_element(*args)
        if element:
            element.clear()
            element.send_keys(value)
            return True
        return False

    def click(self, *args):
        """
        点击页面中对应的元素
        :param args: 传参格式：*(By.ID, 'user')
        :return:
        """
        element = self.driver.find_element(*args)
        if element:
            element.click()
            return True
        else:
            return False

    def execute_js(self, js, *args):
        """执行 js 脚本"""
        element = self.driver.find_element(*args)
        if element:
            self.driver.execute_script(js, element)
            return True
        else:
            return False

    def switch_to_frame(self, *args):
        frame = self.driver.find_element(*args)
        self.driver.switch_to_frame(frame)
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get(r'https://relsagent.joyi.cn/agent/home/ag/login/page')
#     res = find_elements(driver=driver, locate_type='XPATH', value='//*[@id="pwdFrm123"]')
#     print(type(res))
