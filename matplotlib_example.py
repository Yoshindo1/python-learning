# -*- coding: utf-8 -*-

# %% import only : Shift + Enter for Executing each cell
import numpy as np
import matplotlib as mpl # 　Top level of the package
import matplotlib.pyplot as plt #　　pyplot module

# %% setting of the graph
mpl.rcParams['lines.linewidth'] = 10    # 線幅
mpl.rcParams['lines.linestyle'] = '--'  # 破線
mpl.rc('lines', linewidth=10, linestyle='--')

# %% draw graph
t=np.arange(0, 2 * np.pi, 0.1)
plt.figure(1)
plt.plot(t, np.sin(t))
#plt.style.use('ggplot')
plt.style.use('mysty')
plt.show()

# %% Tips 環境設定の記述ファイル
# matplotlibrc : matplotlibの環境設定ファイル。ファイルの参照は次の順で行われる。
# 1.現在のフォルダ。現在のプロジェクトだけに設定したい場合などは、そのプロジェクトフォルダに配置すべし
# 2.ホームフォルダ下にあるMatplotlibの設定保存用フォルダ。
# 3.mpl-dataフォルダ。Matplotlibを更新するたびに上書きされてしまう。設定を残しておくには、個人の設定フォルダにコピーしておくこと。

# mpl.get_configdir() # 設定保存用フォルダ(2.)を表示
# mpl.matplotlib_fname()  #　設定ファイル名を表示
