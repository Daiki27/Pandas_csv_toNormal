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
##っこ
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'CSV_Normalization.ipynb'])

# pd.read_tableでtxtファイルを読み込める.
# df.info()でデータ情報を見れる.
#アイウエオかきく
df = pd.read_csv("teach_data.csv", skiprows = 0, header = None)
df

#df["Unnamed: 1"]
#前処理に時間かかる. たぶんcsv作るときにもっと工夫しないとね.
df = df.rename(columns={
    "20": "SIFT",
    "Unnamed: 1": "V_ave",
    "Unnamed: 2": "V_var",
    "Unnamed: 3": "Edge_ave",
    "Unnamed: 4": "Edge_var",
    "Unnamed: 5": "L_ave",
    "Unnamed: 6": "L_var",
    "Unnamed: 7": "L_ske",
    "Unnamed: 8": "L_kur",
    "Unnamed: 9": "L_10",
    "Unnamed: 10": "L_50",
    "Unnamed: 11": "L_90",
    "Unnamed: 12": "Metalness"
})

import numpy as np
#floatで読み込まないと輝度情報が, ビットの関係で０になる.
df = pd.read_csv("teach_data.csv", skiprows = 0, dtype = np.float64)
df_original = df.copy() #参照理由でコピーでないと.
for i in range(len(df.columns)):
    if(df.columns[i]!="Unnamed: 12"):
        #最大・最小を習得.
        col_name = df.columns[i] # df.columns[i] : 列名
        MAX = df[col_name].max() 
        MIN = df[col_name].min()
        for j in range(len(df[col_name])):
            df.at[j, col_name] = (df.at[j, col_name] - MIN) / (MAX-MIN) 

df

#書き込み
df.to_csv("result.csv",header=False, index=False)


