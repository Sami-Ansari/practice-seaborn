from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset('tips')

sns.violinplot(x='day',y='total_bill', data = var )
# sns.violinplot(x='day',y='total_bill', data = var ,hue='time')
plt.show()

