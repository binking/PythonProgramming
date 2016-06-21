#!../bin/python

import re, requests, datetime, json, JsonParser
from urllib import request
import pandas as pd
from pandas import DataFrame, Series

def LagouSpider(keyword):
    lagou_url = "http://www.lagou.com/jobs/positionAjax.json?px=default&first={tp}&kw={kw}&pn={pn}"

    # Preprocess keyword -- transfer it into utf-8 format and add it to lagou url
    kw_bytes = keyword.encode('utf-8')
    kw_bytes = str(kw_bytes).replace(r'\x', '%').replace(r' ', '')
    kw_in_url = re.sub(r'^b', '', kw_bytes)

    # count how many results by key "totalcount" << "positionResult" << "content" in json file
    page_num = 0
    first_url = lagou_url.format(tp='true', kw=kw_in_url, pn=str(page_num+1))
    with request.urlopen(first_url) as uf:
        json_data = json.loads(str(uf.read(),encoding='utf-8',errors='ignore'))
        resultsCount=int(json_data.get('content', {}).get('positionResult', {}).get('totalCount', 0))
        print('本次搜索页面共计%d' % resultsCount)
    if resultsCount == 0:
        print("Query Keyword error or index key word error")
        return -1

    # Game is on, let's scrap
    for i in range(3):
        if i == 0:
            tp = 'true'
        else:
            tp = 'false'
        url = lagou_url.format(tp=tp, kw=kw_in_url, pn=str(i+1))

        with request.urlopen(url) as uf:
            data = uf.read()
        try:
            totaldata = JsonParser.JsonParser(data)
        except Exception as e:
            continue
    #开始写入数据库
    print(totaldata)
    totaldata.to_excel('lagou.xls',sheet_name='sheet1')

if __name__=="__main__":
    LagouSpider("算法研发")
