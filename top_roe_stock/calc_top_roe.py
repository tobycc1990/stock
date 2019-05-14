#!/usr/bin/python
#!coding:utf-8

import sys
import os
import math
import datetime
#python calc_top_roe.py basic_data report_data day_data

now_year = datetime.datetime.now().year
now_month = datetime.datetime.now().month
now_day = datetime.datetime.now().day
daystr = "%.4d%.2d%.2d" % (now_year - 2, now_month, now_day)

basic_file_name = sys.argv[1]
report_file_name = sys.argv[2]
day_file_name = sys.argv[3]

basic_file = open(basic_file_name)
basic_lines = basic_file.readlines()
basic_file.close()

report_file = open(report_file_name)
report_lines = report_file.readlines()
report_file.close()

day_file = open(day_file_name)
day_lines = day_file.readlines()
day_file.close()

stock_dict = {}
indust_dict = {}

for each_basic_line in basic_lines[1:]:
    each_attr = each_basic_line.strip().split(',')
    code = each_attr[0]
    name = each_attr[1]
    industry = each_attr[2]
    timeToMarket = each_attr[15]
    if not stock_dict.has_key(code):
        stock_dict[code] = {}
    stock_dict[code]["name"] = name
    stock_dict[code]["indust"] = industry
    stock_dict[code]["timeToMarket"] = timeToMarket

    if not indust_dict.has_key(industry):
        indust_dict[industry] = []
    indust_dict[industry].append(code)

for each_report_line in report_lines[1:]:
    each_attr = each_report_line.strip().split(',')
    code = each_attr[1]
    roe = each_attr[6]
    if roe.strip() == "":
        #print "WARNING: %s with null roe" % code
        continue
    if not stock_dict.has_key(code):
        #print "WARNING: %s in report not in basic" % code
        continue
    stock_dict[code]["roe"] = float(roe)

for each_day_line in day_lines[1:]:
    each_attr = each_day_line.strip().split(',')
    code = each_attr[1]
    mktcap = each_attr[-2]
    if not stock_dict.has_key(code):
        #print "WARNING: %s in daily not in basic" % code
        continue
    stock_dict[code]["mktcap"] = float(mktcap)

print "股票行业,股票号码,股票名称,上市日期,市值,ROE"
#for each_indust in indust_dict.keys():
#    for each_code in indust_dict[each_indust]:
#        name = stock_dict[each_code]["name"]
#        timeToMarket = stock_dict[each_code]["timeToMarket"]
#        mktcap = -1
#        if stock_dict[each_code].has_key("mktcap"):
#            mktcap = stock_dict[each_code]["mktcap"] / 10000
#        roe = -1
#        if stock_dict[each_code].has_key("roe"):
#            roe = stock_dict[each_code]["roe"]
#        print "%s,%s,%s,%s,%.2f,%.2f" % (each_indust, each_code, name, timeToMarket, mktcap, roe)

for each_indust in indust_dict.keys():
    indust_result = []
    for each_code in indust_dict[each_indust]:
        name = stock_dict[each_code]["name"]
        timeToMarket = stock_dict[each_code]["timeToMarket"]
        
        mktcap = -1
        if stock_dict[each_code].has_key("mktcap"):
            mktcap = stock_dict[each_code]["mktcap"] / 10000
        stock_dict[each_code]["mktcap"] = mktcap

        roe = -1
        if stock_dict[each_code].has_key("roe"):
            roe = stock_dict[each_code]["roe"]
        stock_dict[each_code]["roe"] = roe

        if roe > 0:
            temp = (each_code, roe)
            indust_result.append(temp)
    #print each_indust
    #print indust_result
    indust_result_sort = sorted(indust_result, key = lambda x: x[1], reverse = True)
    #print indust_result_sort
    lenth = len(indust_result_sort)
    top_count = int(math.ceil(float(lenth) / 5))
    indust_result_top = indust_result_sort[0:top_count]
    #print indust_result_top
    if top_count > 0:
        for each_stock in indust_result_top:
            stock_indust = each_indust
            stock_code = each_stock[0]
            stock_name = stock_dict[stock_code]["name"]
            stock_time = stock_dict[stock_code]["timeToMarket"]
            stock_mktcap = stock_dict[stock_code]["mktcap"]
            stock_roe = stock_dict[stock_code]["roe"]
            if stock_mktcap >= 800 and stock_time <= daystr:
                print "%s,%s,%s,%s,%.2f,%.2f" % (stock_indust, stock_code, stock_name, stock_time, stock_mktcap, stock_roe)
        

