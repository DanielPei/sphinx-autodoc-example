# !/bin/python
# -*- coding:utf-8 -*-

# @Author  : Daniel.Pei
# @Email   : peixq1222@icloud.com
# @Created : 03/05/2019 23:36

import time


def show_time(is_print=True):
    """
    Show Current time.

    :param bool is_print: whether print the time value. Default is True.
    :return: current time val
    :rtype: str
    """
    cur_time = time.time()
    if is_print:
        print(cur_time)
    return cur_time


if __name__ == '__main__':
    show_time()
