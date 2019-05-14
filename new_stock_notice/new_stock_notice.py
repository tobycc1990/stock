#!/usr/bin/python

import sys
import os
import tushare
import time

day_str = time.strftime("%Y-%m-%d", time.localtime())
print "try to get new stock data %s" % day_str
new_stock_list = tushare.new_stocks(retry_count = 100, pause = 30)
new_stock_list.to_csv("./new_stock_data/%s.csv" % day_str, encoding="utf-8")


cmd_str = "source ~/.bash_profile; bce bos cp ./new_stock_data/%s.csv bos:/tobycc-bcc/stock/new_stock_data/%s.csv" % (day_str, day_str)
print cmd_str
os.system(cmd_str)

