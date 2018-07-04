#!/bin/python
# -*- coding: utf-8 -*-#!
import os
import subprocess
#数据恢复
##先prepare,作用是通过回滚未提交的事物至数据文件处于一致性状态
###innobackupex --apply-log /apps/backdb01/2018-06-25_18-30-29/
f = open("./recover.txt")
lines = f.readlines()
input01 = lines[0].split('=')
backupfile1 = input01[1].strip('\n')
print("back:%s"%backupfile1)
print("b")