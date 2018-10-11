#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import os.path
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import shutil


def remove_folder(path):
    if os.path.exists(path):
         shutil.rmtree(path)
print("文件夹删除完毕")  


def del_files(path):
  for root , dirs, files in os.walk(path):
    for name in files:
      if name.endswith(".jpg"):
        os.remove(os.path.join(root, name))
        print("plot图删除完毕") 
        # print ("Delete File: " + os.path.join(root, name)) 
      if name.startswith("grey_"):
        os.remove(os.path.join(root, name))
        print("灰度指标数据删除完毕")   
        # print ("Delete File: " + os.path.join(root, name))
if __name__ == "__main__":
  path = './'
  del_files(path)
  grey = pd.read_csv('greyDate.csv')
  dates = grey['update_date']
  for pth in dates:
      remove_folder(pth)
  print("数据归零")      