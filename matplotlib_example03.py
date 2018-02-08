# リスト9.3　単純な2次元プロット
# -*- coding: utf-8 -*-

# %% import onlyimport numpy as np
import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt
# %% (1) 日本語の基本設定(このスクリプト全体に影響)
mpl.rcParams['font.family']='IPAPMincho'

#-πからπまで0.1刻みの配列を作る
x = np.arange(-np.pi, np.pi, 0.1)
y1 = sin(x)
y2 = cos(x)

plt.figure(1)
plt.clf()

# x,yを描画
plt.plot(x, y1, label='正弦関数') # 凡例にラベルを表示
plt.plot(x, y2, 'r*', markersize=10, label='余弦関数')

#　軸ラベル設定
plt.xlabel('x軸')
plt.ylabel('y軸')

# 凡例の描画
plt.legend(loc='best')
# %% 描画
plt.show()
