# -*- coding: utf-8 -*-
__author__ = 'lizhen'
from DAO import readWeiboData
from DAO import writeWeiboData_ByNLP
from snownlp import SnowNLP

def sentiments():
    countnumber = readWeiboData.count()[0]
    for i in range(1,countnumber):
        textdata = readWeiboData.getText(i)
        # textdata = str(textdata).split('http')[0:-1]
        text = str(textdata).decode('utf8')
        text = SnowNLP(text)
        sentiments = text.sentiments

        writeWeiboData_ByNLP.sentimentsWriteToSql(sentiments,i)
