"""
python数据分析
pandas学习
author: xys
version: 2.0
date: 2019-10-05
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = './文本文件/IMDB-Movie-Data.csv'

df = pd.read_csv(filename)
# print(df.info())
temp_list = df['Genre'].str.split(',').tolist()
genre_list = list(set([i for j in temp_list for i in j]))
# zeros中的参数应该传入shape，其类型为元组
genre_dataFrame = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)

for i in range(df.shape[0]):
    genre_dataFrame.loc[i, temp_list[i]] = 1

final_data = genre_dataFrame.sum(axis=0)
final_data = final_data.sort_values()
# print(final_data.astype(int))
# print(type(final_data.index))

plt.figure(figsize=(20, 8), dpi=100)
plt.bar(final_data.index, final_data, color='cyan', width=0.5)
plt.show()
