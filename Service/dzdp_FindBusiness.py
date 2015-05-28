# -*- coding: utf-8 -*-
__author__ = 'lizhen'
import hashlib
import urllib
from DAO import conMySql
import json
def find_business():
    #请替换appkey和secret
    appkey = "0774328852"
    secret = "d0b762b037dd433284fa87f00a267de1"
    apiUrl = "http://api.dianping.com/v1/business/find_businesses"

    #传入参数
    poiinfolist = conMySql.getPoiInfo(conMySql.openSQL())

    paramSet = []
    paramSet.append(("latitude", poiinfolist[2]))
    paramSet.append(("longitude", poiinfolist[3]))

    #参数排序与拼接
    paramMap = {}
    for pair in paramSet:
        paramMap[pair[0]] = pair[1]

    codec = appkey
    for key in sorted(paramMap.iterkeys()):
        codec += key + paramMap[key]

    codec += secret

    #签名计算
    sign = (hashlib.sha1(codec).hexdigest()).upper()

    #拼接访问的URL
    url_trail = "appkey=" + appkey + "&sign=" + sign
    for pair in paramSet:
        url_trail += "&" + pair[0] + "=" + pair[1]

    requestUrl = apiUrl + "?" + url_trail

    #模拟请求
    response = urllib.urlopen(requestUrl)
    data = json.loads(response.read())
    # print data
    return data


