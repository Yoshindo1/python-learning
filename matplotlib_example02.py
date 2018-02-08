# リスト9.2　特定の箇所だけフォントを変える設定
# -*- coding: utf-8 -*-

# %% import onlyimport numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# %% (1) 日本語の基本設定(このスクリプト全体に影響)
mpl.rcParams['font.family']='IPAGothic'

#    (2) 指定箇所のみ有効にする日本語設定
font_path = 'C:\\Users\\mamiko\\Anaconda3\\lib\\site-packages\\matplotlib\\mpl-data\\fonts\\ttf\\ipam.ttf'
font_prop = fm.FontProperties(fname=font_path)
font_prop.set_style('normal')
font_prop.set_size('16')
# %% draw graph
plt.figure(1)
# Xラベルは(1)の設定が有効
plt.plot([1,2,3],[2,5,9])
# Yラベルは(2)の設定が有効
plt.ylabel('日本語のY軸ラベル',fontproperties=font_prop)