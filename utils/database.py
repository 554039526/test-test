# -*- coding: utf-8 -*-
"""
    @File: database.py
    @Desc: 
    @Time: 2021/11/18 9:18 下午
    @Author: Wan Wenlong
"""
import pymssql
from utils.util import getItemsSection


database_info = getItemsSection('sqlserver')


def select(query):
    try:
        with pymssql.connect(server=database_info['host'], port=database_info['port'], database=database_info['database'],
                             user=database_info['user'], password=database_info['password']) as conn:
            with conn.cursor(as_dict=True) as cursor:
                cursor.execute(query)
                res = cursor.fetchall()
                return res
    except Exception as error:
        print(f'Database error: {error}')


if __name__ == '__main__':
    res = select('select list_master_id from list_listing_master where listing_no = 404559091055210496')
    print(res)



