# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
import subprocess
import numpy as np

# pd.read_tableでtxtファイルを読み込める.
# df.info()でデータ情報を見れる.
df = pd.read_csv("teach_data.csv", skiprows = 0, header = None)
df

#floatで読み込まないと輝度情報が, ビットの関係で０になる.
df = pd.read_csv("teach_data.csv", skiprows = 0, dtype = np.float64)
df_original = df.copy() 
for i in range(len(df.columns)):
    if(df.columns[i]!="Unnamed: 12"):
        #最大・最小を習得.
        col_name = df.columns[i] # df.columns[i] : 列名
        MAX = df[col_name].max() 
        MIN = df[col_name].min()
        for j in range(len(df[col_name])):
            #最大・最小で正規化.
            df.at[j, col_name] = (df.at[j, col_name] - MIN) / (MAX-MIN) 
#書き込み
df.to_csv("result.csv",header=False, index=False)

df
