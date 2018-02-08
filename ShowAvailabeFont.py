# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 22:45:27 2018
現在matplotlibが使えるフォントの名前の一覧を表示する
@author: mamiko
"""

import matplotlib as mpl
font_paths = mpl.font_manager.findSystemFonts()
font_objects = mpl.font_manager.createFontList(font_paths)
font_names = [f.name for f in font_objects]
print(font_names)