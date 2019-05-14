#!/usr/bin/python 
#!coding:utf-8

import sys
import os

price_file = open("./price")
price_lines = price_file.readlines()
price_file.close()

bvps_file = open("./bvps")
bvps_lines = bvps_file.readlines()
bvps_file.close()

stock_dict = {}

for each_bvps_line in bvps_lines:
    stock_number, stock_name, stock_indust, bvps = each_bvps_line.strip().split(',')
    #print stock_number, stock_name, bvps, stock_indust
    if not stock_dict.has_key(stock_number):
        stock_dict[stock_number] = {}
    stock_dict[stock_number]["name"] = stock_name
    stock_dict[stock_number]["bvps"] = float(bvps)
    stock_dict[stock_number]["indust"] = stock_indust

for each_price_line in price_lines:
    stock_number, price = each_price_line.strip().split(',')
    stock_dict[stock_number]["price"] = float(price)

print "股票号码,股票名称,股票行业,当前价格,每股净资产,净资产/价格,价格-净资产,(价格-净资产)/价格"
for stock_number in stock_dict.keys():
    bvps_offset = stock_dict[stock_number]["price"] - stock_dict[stock_number]["bvps"]
    bvps_offset_percent = 999999
    if stock_dict[stock_number]["price"] > 0:
        bvps_offset_percent = bvps_offset / stock_dict[stock_number]["price"]
        print "%s,%s,%s,%.2f,%.2f,%.2f,%.2f,%.2f" % (stock_number,
                stock_dict[stock_number]["name"],
                stock_dict[stock_number]["indust"],
                stock_dict[stock_number]["price"],
                stock_dict[stock_number]["bvps"],
                stock_dict[stock_number]["bvps"]/stock_dict[stock_number]["price"],
                bvps_offset, bvps_offset_percent)
        
