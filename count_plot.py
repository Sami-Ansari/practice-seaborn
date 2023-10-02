from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset('tips')

# print(var)

sns.countplot(x=var.sex, hue = var.smoker)
# for hor pas y instead of x 
# sns.countplot(y=var.sex, hue = var.smoker)

plt.show()
