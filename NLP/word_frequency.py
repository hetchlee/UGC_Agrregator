# -*- coding: utf-8 -*-
__author__ = 'lizhen'
from DAO import conMySql
from DAO import readWeiboData
import jieba
import matplotlib.pyplot as pyplot
import matplotlib
def frequency():
    textdict={}
    countnumber = readWeiboData.count()[0]
    for i in range(1,countnumber):
        textdata = readWeiboData.getText(i)
        for word in jieba.cut(textdata):
            word = word.encode('utf8')
            textdict[word] = textdict.get(word, 0) + 1
    return textdict

def frequencytotxt():
    textdict=frequency()
    f=open('D:\wuhuweibodict.txt','w')
    for i in textdict.keys():
        f.write (str(textdict[i])+'\t'+i+'\n')
    f.close()
