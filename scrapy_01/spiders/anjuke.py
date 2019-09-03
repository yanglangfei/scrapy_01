# -*- coding: utf-8 -*-
# Scrapy spider 模块
# 采集安居客房源信息
# 采集结果保存在anjuke-result.xml中
# https://segmentfault.com/a/1190000007307030
import scrapy
import os
import time
from gooseeker import GsExtractor


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://bj.zu.anjuke.com/fangyuan/p1']

    def parse(self, response):
        print("-" * 10)
        # 引入Gooseeker最新规则提取器
        bbsExtra = GsExtractor()
        # 设置xslt抓取规则
        bbsExtra.setXsltFromAPI("31d24931e043e2d5364d03b8ff9cc77e", "安居客_房源")
        # 调用extract方法提取所需内容
        result = bbsExtra.extractHTML(response.body)
        # 打印采集结果
        res = str(result).encode('gbk', 'ignore').decode('gbk')
        print(res)
        # 保存采集结果
        file_path = os.getcwd() + "/anjuke-result.xml"
        open(file_path, "wb").write(result)
        # 打印结果存放路径
        print("采集结果文件：" + file_path)
