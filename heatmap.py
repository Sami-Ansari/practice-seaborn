from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

var = np.linspace(1,10,20).reshape(4,5)
# print(var)

data1 = sns.load_dataset('anagrams')
# first convert the data in 2 dimenstion
# x = data1.drop(columns = ["attnr"] ,axis=1).head(10)
# print(data)

# sns.heatmap(var,vmin=0,vmax=12,cmap = 'PuOr',annot=True)

ar = np.array([["a0","a1",'a2','a3','a4'],
               ['b0','b1','b2','b3','b4']])
sns.heatmap(var,vmin=0,vmax=10,cmap = 'PuOr',annot=True,fmt ="s" )
# for custom annot fmt zarori hy
# annot=True show values in heatmap
# sns.heatmap(x)
plt.show()