#!/usr/bin/python

import sys
import os
import tushare
import time

day_str = time.strftime("%Y-%m-%d", time.localtime())
print "try to get stock today all data %s" % day_str
today_list = tushare.get_day_all()
today_list.to_csv("./today_data/%s.csv" % day_str, encoding="utf-8")

basic_list = tushare.get_stock_basics()
basic_list.to_csv("./basic_data/%s.csv" % day_str, encoding="utf-8")



#cmd_str = "source ~/.bash_profile; bce bos cp ./new_stock_data/%s.csv bos:/tobycc-bcc/stock/new_stock_data/%s.csv" % (day_str, day_str)
#print cmd_str
#os.system(cmd_str)

