#!/usr/bin/python

import sys
import os
import tushare
import time

day_str = time.strftime("%Y-%m-%d", time.localtime())
basic_list = tushare.get_today_all()
basic_list.to_csv("./day-%s.csv" % day_str, encoding="utf-8")
