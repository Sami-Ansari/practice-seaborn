from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset("penguins")

# print(var)

sns.displot(var['flipper_length_mm'] ,
            bins = [170,180,190,200,210,220,230,240] ,
            kde = True , rug = True,color = 'g')
# parameter pass in dis 
# rug for color density kde for line color for changing color
#  log scale for log chart
plt.show()