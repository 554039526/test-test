# -*- coding: utf-8 -*-
"""
    @File: run.py
    @Desc: 
    @Time: 2021/10/22 上午9:50
    @Author: Wan Wenlong
"""
import pytest
from utils.util import *


if __name__ == '__main__':

    flag = input(f'请选择执行方式: \n1.正常执行；\n2.执行特定标签的测试用例\n请输入:')
    # 执行测试
    if flag == '1':  # 正常执行
        pytest.main(['-v', '--log-file={}'.format(log_name),
                     '--html={}'.format(report_name), '--self-contained-html', cases_path])

    elif flag == '2':  # 执行特殊标签的测试用例
        marks = get_data('pytest', 'markers')
        print('可供选择的标签：{}'.format(marks))
        mark = input('请输入要执行的标签：')

        if mark in marks:
            pytest.main(['-v', '-m {}'.format(mark), '--log-file={}'.format(log_name),
                        '--html={}'.format(report_name), '--self-contained-html', cases_path])
        else:
            print('输入的标签不存在')

    else:
        print('输入错误，请重新运行')
