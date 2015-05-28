# -*- coding: utf-8 -*-
__author__ = 'lizhen'
from DAO import readWeiboData
from DAO import writeWeiboData
from snownlp import SnowNLP
def keywords():
    countnumber = readWeiboData.count()[0]
    for i in range(1,countnumber):
        textdata = readWeiboData.getText(i)
        # textdata = str(textdata).split('http')[0:-1]
        text = str(textdata).decode('utf8')
        text = SnowNLP(text)
        texttosql = ''
        for j in range(0,len(text.keywords(3))):
            texttosql+=text.keywords(3)[j]+" "

        writeWeiboData.keywordsWriteToSql(texttosql,i)