# withブロックの中にだけスタイルを適用する
# %% import only : Shift + Enter for Executing each cell
import numpy as np
import matplotlib.pyplot as plt #　　pyplot module

# %% setting of the graph
#mpl.rcParams['lines.linewidth'] = 10    # 線幅
#mpl.rcParams['lines.linestyle'] = '--'  # 破線
#mpl.rc('lines', linewidth=10, linestyle='--')

# %% draw graph
x=np.arange(0, np.pi, 0.01)
# withブロックの中にだけスタイルを適用する
with plt.style.context('dark_background'):
    plt.plot(x, np.sin(x))

# %% Tips 環境設定の記述ファイル
# matplotlibrc : matplotlibの環境設定ファイル。ファイルの参照は次の順で行われる。
# 1.現在のフォルダ。現在のプロジェクトだけに設定したい場合などは、そのプロジェクトフォルダに配置すべし
# 2.ホームフォルダ下にあるMatplotlibの設定保存用フォルダ。
# 3.mpl-dataフォルダ。Matplotlibを更新するたびに上書きされてしまう。設定を残しておくには、個人の設定フォルダにコピーしておくこと。

# mpl.get_configdir() # 設定保存用フォルダ(2.)を表示
# mpl.matplotlib_fname()  #　設定ファイル名を表示
