# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 22:10:13 2018

@author: mamiko
"""

import matplotlib.pyplot as plt

#(2) 指定箇所のみ有効にする日本語設定
font_path = 'C:\\Users\\mamiko\\Anaconda3\\lib\\site-packages\\matplotlib\\mpl-data\\fonts\\ttf\\ipam.ttf'
font_prop = fm.FontProperties(fname=font_path)
font_prop.set_style('normal')
font_prop.set_size('16')
plt.figure()
plt.xlabel('x軸',fontproperties=font_prop)
plt.ylabel('y軸',fontproperties=font_prop)