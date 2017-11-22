# coding=utf-8
# -*- coding: UTF-8 -*-
import sys
import codecs
from langconv import *
import os

reload(sys)
sys.setdefaultencoding('utf-8')


def fan2jian(file_path):
    # 转换繁体到简体
    def cht_to_chs(line):
        line = Converter('zh-hans').convert(line)
        line.encode('utf-8')
        return line

    f = codecs.open(file_path, 'r', encoding='utf8')
    linesFan = f.read()
    f.close()
    linesJian = cht_to_chs(linesFan)
    f = codecs.open(file_path, 'w', encoding='utf8')
    f.write(linesJian)
    f.close()





# 转换简体到繁体
def chs_to_cht(line):
    line = Converter('zh-hant').convert(line)
    line.encode('utf-8')
    return line


rootdir = '/Users/sunbo/Desktop/四库全书/result/'
list = os.listdir(rootdir)
for sub_folder in list:
    sub_folder_path = os.path.join(rootdir, sub_folder)
    if os.path.isdir(sub_folder_path):
        files = os.listdir(sub_folder_path)
        for f in files:
            file_path = os.path.join(sub_folder_path, f)
            if os.path.isfile(file_path):
                #print file_path
                fan2jian(file_path)
