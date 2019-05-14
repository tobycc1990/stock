#!/usr/bin/python

import sys
import os
import tushare
import time

day_str = time.strftime("%Y-%m-%d", time.localtime())
basic_list = tushare.get_report_data(2018, 4)
basic_list.to_csv("./report_data_%s.csv" % day_str, encoding="utf-8")
